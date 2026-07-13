# Voxarium Software Architecture Specification

Document Path:
spec/200_Application/Generation_Service.md

Document ID: APP-018

Title: Generation Service

Version: 1.0.0

Status: Accepted

Classification: Normative

Depends On

- DOM-104 Text Fragment
- DOM-105 Character
- DOM-106 Voice Profile
- APP-017 Project Service
- APP-016 Workflow Engine
- APP-008 Job Orchestrator
- APP-014 Plugin Runtime
- TTS Plugin Contract

Referenced By

- TTS Engine Plugins
- Timeline Module
- Audio Processing Module
- Export Module
- UI Layer

---

# 1. Purpose

Generation Service является основным прикладным сервисом Voxarium, отвечающим за преобразование текстового содержимого проекта в аудиоматериал.

Основная задача:

```
Text

↓

Analysis

↓

Voice Selection

↓

TTS Generation

↓

Audio Asset

```

Generation Service является координатором процесса генерации.

Он не содержит собственных алгоритмов синтеза речи.

---

# 2. Main Concept

Voxarium предназначен для создания озвучки различных типов:

- аудиокниги;
- субтитры;
- сценарии;
- диалоги;
- обучающие материалы;
- игровые сценарии;
- документальные материалы.

Поэтому генерация должна быть построена вокруг универсальной модели:

```
Text Fragment

↓

Generation Request

↓

Voice Assignment

↓

TTS Capability

↓

Generated Audio

```

---

# 3. Responsibilities

Generation Service отвечает за:

- подготовку текста;
- создание Generation Job;
- выбор голосового профиля;
- передачу параметров TTS Plugin;
- обработку результатов;
- сохранение Audio Asset;
- связь текста и аудио.

Generation Service не отвечает за:

- реализацию TTS;
- загрузку моделей;
- управление GPU;
- обработку низкоуровневого аудио.

---

# 4. Architectural Position

```
Project

↓

Generation Service

↓

Job Orchestrator

↓

Worker

↓

TTS Plugin

↓

Voice Engine

↓

Audio Asset

```

---

# 5. Generation Pipeline

Полный процесс:

```
Input Text

↓

Text Preparation

↓

Segmentation

↓

Role Detection

↓

Voice Assignment

↓

Generation Jobs

↓

TTS Execution

↓

Audio Validation

↓

Asset Creation

↓

Timeline Update

```

---

# 6. Text Preparation

Перед генерацией выполняется подготовка текста.

Включает:

- очистку;
- нормализацию;
- исправление переносов;
- обработку специальных символов;
- подготовку пунктуации.

---

# 7. Text Segmentation

Большой текст разделяется на Fragment.

Причины:

- ограничение моделей;
- параллельная генерация;
- повторная генерация части текста;
- удобство редактирования.

---

# 8. Fragment Model

Fragment является минимальной единицей генерации.

Содержит:

```
Fragment ID

Text

Position

Character

Voice Profile

Generation Status

Audio Asset

```

---

# 9. Fragment Size

Размер Fragment определяется:

- выбранным TTS Plugin;
- языком;
- настройками качества;
- ограничением модели.

Пример:

```
XTTS

≈ несколько предложений

```

---

# 10. Role Detection

Generation Service поддерживает определение ролей.

Пример:

Текст:

```
— Кто ты?

— Я пришёл помочь.

```

Результат:

```
Character A

Character B

```

---

# 11. Role Assignment

Каждый Fragment может иметь:

- автора;
- персонажа;
- диктора.

Пример:

```
Narrator

↓

Default Voice


Hero

↓

Voice Profile A


Villain

↓

Voice Profile B

```

---

# 12. Voice Profile Selection

Voice Profile выбирается из:

- Project Settings;
- Character Settings;
- User Selection;
- Workflow Parameters.

---

# 13. Generation Request

Перед запуском создаётся объект:

```
Generation Request

{

Fragment ID

Voice Profile

Language

Style

Emotion

Speed

Pitch

Engine

}

```

---

# 14. TTS Capability Resolution

Generation Service не вызывает конкретный движок.

Он запрашивает Capability:

```
Speech.Generation

Language: Russian

Voice Clone: true

Quality: High

```

Plugin Runtime выбирает подходящий Plugin.

---

# 15. Multiple TTS Engines

Проект может использовать разные движки.

Пример:

```
Narrator

↓

XTTS


Characters

↓

StyleTTS


Special Effects

↓

Voice Conversion Plugin

```

---

# 16. Batch Generation

Поддерживается пакетная генерация:

```
Chapter 1

 ├── Fragment 1

 ├── Fragment 2

 └── Fragment 3


Chapter 2

 ├── Fragment 1

 └── Fragment 2

```

---

# 17. Parallel Generation

Независимые Fragment могут выполняться параллельно.

Решение принимает:

Scheduler.

Generation Service только создаёт Job.

---

# 18. Generation Parameters

Поддерживаются:

## Voice

- speaker;
- clone;
- style.


## Speech

- speed;
- pitch;
- emotion;
- language.


## Quality

- sample rate;
- model quality;
- enhancement.

---

# 19. Result Handling

После генерации:

```
Audio File

↓

Validation

↓

Metadata Extraction

↓

Audio Asset

↓

Timeline Update

```

---

# 20. Audio Validation

Проверяется:

- файл существует;
- формат корректен;
- длительность;
- отсутствие повреждений;
- соответствие параметрам.

---

# 21. Regeneration

Пользователь может:

- перегенерировать Fragment;
- изменить голос;
- изменить параметры;
- использовать другой Engine.

---

# 22. Versioning

Каждая генерация создаёт версию.

Пример:

```
Fragment 15

Version 1

XTTS


Version 2

StyleTTS


Version 3

Custom Voice

```

---

# 23. Generation History

Хранится:

- дата;
- Engine;
- Voice;
- параметры;
- результат;
- ошибки.

---

# 24. Event Integration

Generation Service публикует:

```
GenerationRequested

GenerationStarted

FragmentGenerated

GenerationCompleted

GenerationFailed

```

---

# 25. Workflow Integration

Workflow может использовать:

```
GenerateText

GenerateChapter

GenerateProject

RegenerateFragment

```

---

# 26. Plugin Integration

TTS Plugin предоставляет:

```
Speech.Generation

```

Generation Service работает только через этот контракт.

---

# 27. Performance Requirements

Generation Service должен поддерживать:

- большие книги;
- тысячи Fragment;
- параллельную генерацию;
- повторную генерацию отдельных частей.

---

# 28. Test Requirements

Проверяются:

- создание Generation Request;
- выбор голоса;
- роли;
- Fragment;
- ошибки TTS;
- повторная генерация;
- сохранение истории.

---

# 29. Compliance

Любая реализация Generation Service обязана соответствовать настоящему документу.

---

# Appendix A. Audiobook Example

Input:

```
Chapter 1

Narrator:
The room was silent.

Hero:
I must leave.

```

Analysis:

```
Fragment 1

Character:
Narrator


Fragment 2

Character:
Hero

```

Generation:

```
Fragment 1

↓

Narrator Voice


Fragment 2

↓

Hero Voice

```

Output:

```
chapter_001.wav

```

---

End of Document