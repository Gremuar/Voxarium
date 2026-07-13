# Voxarium Software Architecture Specification

Document Path:
spec/200_Application/Configuration_Service.md

Document ID: APP-025

Title: Configuration Service

Version: 1.0.0

Status: Accepted

Classification: Normative

Depends On

- APP-001 Application Architecture
- APP-014 Plugin Runtime
- APP-017 Project Service
- APP-012 Resource Manager
- Persistence Layer

Referenced By

- Core Application
- UI Layer
- Plugin System
- Workflow Engine
- Generation Service
- Audio Service
- Export Service

---

# 1. Purpose

Configuration Service является подсистемой централизованного управления настройками Voxarium.

Основная задача:

обеспечить единый механизм хранения, загрузки, изменения и применения конфигурации всех компонентов системы.

---

# 2. Main Concept

В Voxarium существует несколько уровней настроек.

Настройки не должны смешиваться.

Модель:

```
Application Configuration

        ↓

User Configuration

        ↓

Project Configuration

        ↓

Module Configuration

        ↓

Runtime Configuration

```

---

# 3. Responsibilities

Configuration Service отвечает за:

- хранение настроек;
- загрузку конфигурации;
- изменение параметров;
- применение настроек;
- управление версиями конфигурации;
- миграцию старых настроек.

Configuration Service не отвечает за:

- бизнес-логику;
- выполнение задач;
- хранение пользовательских данных проектов.

---

# 4. Configuration Layers

## 4.1 Application Configuration

Глобальные настройки приложения.

Примеры:

```
Application Language

Default Paths

Logging Level

Cache Location

Update Policy

```

---

## 4.2 User Configuration

Настройки пользователя.

Примеры:

```
Interface Theme

Recent Projects

Default Export Format

Preferred Voices

Keyboard Shortcuts

```

---

## 4.3 Project Configuration

Настройки конкретного проекта.

Примеры:

```
Language

Default Narrator

Audio Quality

Generation Rules

Export Defaults

```

---

## 4.4 Plugin Configuration

Настройки расширений.

Пример:

```
XTTS Plugin

Model Path

GPU Preference

Batch Size

Temperature

```

---

## 4.5 Runtime Configuration

Временные параметры:

```
Current GPU

Active Workers

Temporary Limits

Execution Options

```

---

# 5. Configuration Hierarchy

При получении параметра используется порядок:

```
Runtime Override

↓

Project Setting

↓

User Setting

↓

Application Default

```

---

# 6. Configuration Object

Каждая настройка имеет:

```
Configuration Key

Value

Type

Scope

Version

Source

Modified Date

```

---

# 7. Configuration Keys

Используется иерархическая схема.

Пример:

```
tts.xtts.model_path

tts.xtts.batch_size

audio.mastering.lufs

export.m4b.cover

```

---

# 8. Type System

Поддерживаются:

```
String

Integer

Float

Boolean

Enum

Path

List

Object

Secret

```

---

# 9. Validation

Перед сохранением:

проверяется:

- тип;
- допустимый диапазон;
- обязательность;
- совместимость.

---

# 10. Default Values

Каждый модуль должен иметь:

```
Default Configuration

```

Пример:

Plugin:

```
Default:

sample_rate=24000

```

---

# 11. Configuration Schema

Каждый модуль описывает схему.

Пример:

```
audio.processing

{

noise_reduction:

boolean


lufs_target:

number

}

```

---

# 12. Dynamic Configuration

Часть настроек может изменяться во время работы.

Например:

```
Worker Limit

GPU Selection

Log Level

```

---

# 13. Static Configuration

Некоторые параметры требуют перезапуска:

```
Database Location

Plugin Directory

Runtime Engine

```

---

# 14. Secret Management

Чувствительные данные:

- API ключи;
- токены;
- пароли.

Должны храниться отдельно.

Пример:

```
Secret Storage

↓

Configuration Reference

```

---

# 15. Plugin Configuration

Plugin получает настройки через Context.

Запрещено:

```
Plugin

↓

Read random config files

```

Правильно:

```
Plugin

↓

Plugin Context

↓

Configuration Service

```

---

# 16. Project Configuration Migration

При открытии старого проекта:

```
Detect Version

↓

Migration

↓

Load

```

---

# 17. Configuration Versioning

Каждая конфигурация имеет:

```
Schema Version

```

Позволяет:

- обновлять приложение;
- сохранять совместимость.

---

# 18. User Profiles

Поддерживается несколько профилей настроек.

Пример:

```
Audiobook Profile

Video Profile

Podcast Profile

```

---

# 19. Configuration Events

Публикуются:

```
ConfigurationChanged

ConfigurationLoaded

ConfigurationMigrated

ConfigurationInvalid

```

---

# 20. UI Integration

UI использует Configuration Service для:

- отображения настроек;
- изменения параметров;
- сохранения профилей.

---

# 21. Workflow Integration

Workflow может получать параметры:

```
Workflow

↓

Configuration Resolver

↓

Effective Settings

```

---

# 22. Effective Configuration

Перед выполнением создаётся итоговая конфигурация:

Пример:

```
Project:

Language=Russian


User:

Quality=High


Runtime:

GPU=RTX4070Ti


Result:

Generation Configuration

```

---

# 23. Performance Requirements

Configuration Service должен:

- быстро загружаться;
- кэшировать данные;
- не создавать блокировок;
- поддерживать большие проекты.

---

# 24. Recovery

При повреждении:

- использовать резервную копию;
- восстановить defaults;
- сохранить диагностику.

---

# 25. Security

Необходимо защищать:

- секреты;
- пути;
- пользовательские данные.

---

# 26. Test Requirements

Проверяются:

- уровни наследования;
- миграции;
- валидация;
- Plugin settings;
- восстановление.

---

# 27. Compliance

Любая реализация Configuration Service обязана соответствовать настоящему документу.

---

# Appendix A. Example

Настройка генерации:

Application:

```
audio.sample_rate=24000

```

User:

```
tts.quality=high

```

Project:

```
voice.default=narrator

```

Runtime:

```
gpu=0

```

Итог:

```
XTTS Generation Configuration

```

---

End of Document