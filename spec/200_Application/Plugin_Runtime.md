# Voxarium Software Architecture Specification

Document Path:
spec/200_Application/Plugin_Runtime.md

Document ID: APP-014

Title: Plugin Runtime

Version: 1.0.0

Status: Accepted

Classification: Normative

Depends On

- APP-001 Application Architecture
- APP-006 Event Bus
- APP-011 Worker
- APP-013 Execution Runtime
- Plugin Architecture Specification

Referenced By

- TTS Plugin System
- Voice Clone Module
- Audio Processing Plugins
- AI Plugins
- External Integrations
- Plugin Marketplace

---

# 1. Purpose

Plugin Runtime является подсистемой выполнения расширений Voxarium.

Основное назначение Plugin Runtime:

- загрузка Plugin;
- регистрация возможностей;
- управление жизненным циклом;
- изоляция выполнения;
- контроль совместимости;
- взаимодействие Plugin с Core.

Plugin Runtime является единственным механизмом подключения расширений.

---

# 2. Architectural Principle

Core Voxarium не должен содержать специального кода для отдельных технологий.

Запрещается:

```
if engine == XTTS:
    run_xtts()

if engine == Whisper:
    run_whisper()

if engine == CustomAI:
    run_custom()

```

Вместо этого:

```
Capability

↓

Plugin Contract

↓

Plugin Runtime

↓

Plugin Implementation

```

---

# 3. Responsibilities

Plugin Runtime отвечает за:

- обнаружение Plugin;
- проверку Plugin;
- загрузку;
- регистрацию;
- создание Plugin Context;
- управление версиями;
- остановку;
- удаление;
- контроль безопасности.

Plugin Runtime не отвечает за:

- бизнес-логику;
- генерацию речи;
- обработку аудио;
- управление Job.

---

# 4. Plugin Lifecycle

Каждый Plugin проходит следующие состояния:

```
Discovered

↓

Validated

↓

Installed

↓

Loaded

↓

Initialized

↓

Active

↓

Disabled

↓

Unloaded

↓

Removed

```

---

# 5. Plugin Discovery

Plugin могут обнаруживаться из:

- локальной директории;
- встроенного каталога;
- пользовательского каталога;
- удалённого репозитория;
- корпоративного каталога.

---

# 6. Plugin Package

Минимальная структура Plugin:

```
plugin/

├── manifest.json

├── runtime/

├── resources/

├── models/

├── documentation/

└── tests/

```

---

# 7. Plugin Manifest

Каждый Plugin обязан иметь Manifest.

Manifest содержит:

```
Plugin ID

Name

Version

Author

License

Required Voxarium Version

Capabilities

Dependencies

Permissions

Entry Point

```

---

# 8. Plugin ID

Каждый Plugin имеет уникальный идентификатор.

Пример:

```
org.voxarium.tts.xtts

org.voxarium.audio.ffmpeg

org.company.voice.clone

```

ID никогда не меняется после публикации.

---

# 9. Capability Declaration

Plugin описывает предоставляемые возможности.

Пример:

```
Capability:

Speech.Generation


Parameters:

language

speaker

style

sample_rate


Resources:

GPU

VRAM >= 6GB

```

---

# 10. Plugin Types

Минимальные категории:

---

## TTS Plugin

Генерация речи.

Примеры:

- XTTS;
- StyleTTS;
- VITS;
- FastSpeech.

---

## Voice Plugin

Работа с голосом.

Примеры:

- cloning;
- speaker embedding;
- voice conversion.

---

## Audio Plugin

Обработка аудио:

- normalization;
- mixing;
- mastering;
- noise reduction.

---

## Document Plugin

Работа с документами:

- PDF;
- EPUB;
- DOCX;
- subtitles.

---

## AI Plugin

Дополнительные интеллектуальные функции:

- анализ текста;
- определение ролей;
- исправление ошибок.

---

# 11. Plugin Contract

Каждый Plugin реализует внешний контракт.

Минимально:

```
initialize()

getCapabilities()

validate()

execute()

shutdown()

```

---

# 12. Plugin Context

Plugin получает Context.

Context содержит:

- Plugin ID;
- Project Context;
- Resource Access;
- Storage Access;
- Logging;
- Event Publishing;
- Configuration.

---

# 13. Dependency Injection

Plugin не должен искать системные компоненты самостоятельно.

Все зависимости передаются через Context.

---

# 14. Version Compatibility

Plugin Runtime проверяет:

- версию Core;
- версию API;
- версии зависимостей.

Несовместимый Plugin не загружается.

---

# 15. Dependency Management

Plugin может зависеть от:

- других Plugin;
- библиотек;
- моделей;
- Runtime компонентов.

Зависимости должны быть описаны в Manifest.

---

# 16. Isolation Model

Поддерживаются режимы:

---

## InProcess

Для доверенных Plugin.

Преимущества:

- максимальная скорость.

Недостатки:

- меньше изоляции.

---

## OutOfProcess

Для тяжёлых Plugin.

Преимущества:

- защита Core;
- независимый жизненный цикл.

---

## Sandbox

Для сторонних Plugin.

Ограничения:

- файловая система;
- сеть;
- память;
- права доступа.

---

# 17. Permission System

Plugin Manifest должен описывать разрешения.

Пример:

```
filesystem.read.project

filesystem.write.output

gpu.access

network.access

model.load

```

---

# 18. Plugin Communication

Plugin общается с системой только через:

- Plugin API;
- Event Bus;
- Ports;
- Execution Runtime.

Прямой доступ к Core запрещён.

---

# 19. Model Management

AI Plugin может содержать модели.

Plugin Runtime должен поддерживать:

- регистрацию моделей;
- проверку размера;
- загрузку;
- обновление;
- удаление.

---

# 20. Plugin Configuration

Каждый Plugin имеет собственную конфигурацию.

Конфигурация хранится отдельно от Core.

---

# 21. Plugin Updates

Обновление Plugin должно поддерживать:

- проверку подписи;
- миграцию настроек;
- откат версии.

---

# 22. Failure Handling

Если Plugin завершился ошибкой:

Runtime:

1. Останавливает Plugin.
2. Освобождает ресурсы.
3. Сохраняет диагностику.
4. Уведомляет систему.

---

# 23. Event Integration

Plugin Runtime публикует:

```
PluginInstalled

PluginLoaded

PluginStarted

PluginFailed

PluginDisabled

PluginUpdated

```

---

# 24. Security

Plugin Runtime обязан защищать:

- пользовательские данные;
- файлы проекта;
- модели;
- системные ресурсы.

---

# 25. Performance Requirements

Plugin Runtime должен:

- быстро загружать Plugin;
- минимизировать overhead;
- поддерживать большое количество расширений;
- не замедлять Core.

---

# 26. Test Requirements

Проверяются:

- установка;
- загрузка;
- выгрузка;
- несовместимость версий;
- ошибки Plugin;
- права доступа;
- изоляция.

---

# 27. Compliance

Любая реализация Plugin Runtime обязана соответствовать настоящему документу.

---

# Appendix A. Example TTS Plugin

Plugin:

```
org.voxarium.tts.xtts

```

Capabilities:

```
Speech.Generation

Voice.Clone

Language.Russian

```

Requirements:

```
CUDA

GPU

VRAM >= 6GB

```

Execution:

```
GenerateSpeechJob

↓

Worker

↓

Plugin Runtime

↓

XTTS Plugin

↓

XTTS Engine

↓

WAV Output

```

---

End of Document