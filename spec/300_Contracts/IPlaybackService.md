# Voxarium Software Architecture Specification

Document Path:
spec/300_Contracts/IPlaybackService.md

Document ID: CTR-011

Title: IPlaybackService

Version: 1.0.0

Status: Accepted

Classification: Normative

Depends On

- CTR-000 IService
- Timeline
- AudioTrack

Referenced By

- Audio_Service
- Timeline_Service
- User_Interface_Architecture

---

# 1. Purpose

IPlaybackService defines the public Application Service contract responsible for audio playback.

The contract provides transport control, playback state management and navigation across the project timeline.

Playback SHALL NOT modify the Domain Model.

---

# 2. Responsibilities

The service SHALL provide:

- playback control;
- transport control;
- playback state management;
- playback position management;
- timeline navigation;
- playback speed control;
- playback loop control;
- playback volume control.

---

# 3. Non-Responsibilities

The service SHALL NOT:

- synthesize speech;
- process audio;
- modify Timeline;
- edit AudioTrack;
- import or export data.

---

# 4. Playback Operations

## 4.1 Play

### Signature

Play()

### Purpose

Starts playback from the current playback position.

### Preconditions

- Playback source is available.

### Postconditions

- Playback state becomes Playing.

### Published Events

- PlaybackStarted

---

## 4.2 Pause

### Signature

Pause()

### Purpose

Temporarily pauses playback.

### Published Events

- PlaybackPaused

---

## 4.3 Stop

### Signature

Stop()

### Purpose

Stops playback.

### Postconditions

- Playback position remains defined.
- Playback state becomes Stopped.

### Published Events

- PlaybackStopped

---

## 4.4 Seek

### Signature

Seek(TimePosition)

### Purpose

Moves playback position.

### Parameters

- TimelinePosition

### Published Events

- PlaybackPositionChanged

---

## 4.5 SkipForward

### Signature

SkipForward(Duration)

---

## 4.6 SkipBackward

### Signature

SkipBackward(Duration)

---

# 5. Timeline Navigation

The service SHALL provide:

- GoToBeginning
- GoToEnd
- GoToNextSegment
- GoToPreviousSegment
- GoToNextFragment
- GoToPreviousFragment

---

# 6. Playback Configuration

The service SHALL support:

- SetPlaybackSpeed
- GetPlaybackSpeed
- SetPlaybackVolume
- GetPlaybackVolume
- EnableLoop
- DisableLoop
- Mute
- Unmute

---

# 7. Query Operations

The contract SHALL provide:

- GetPlaybackState
- GetPlaybackPosition
- GetCurrentSegment
- GetCurrentFragment
- IsPlaying
- IsPaused
- IsStopped

Queries SHALL NOT modify system state.

---

# 8. Playback State Model

The playback state SHALL be one of:

- Stopped
- Playing
- Paused
- Buffering
- Seeking
- Completed
- Error

Transitions between states SHALL be deterministic.

---

# 9. Synchronization

Playback position SHALL remain synchronized with Timeline.

The implementation SHALL notify subscribers whenever playback position changes.

---

# 10. Transaction Rules

Playback operations SHALL NOT require Application transactions.

---

# 11. Thread Safety

Playback control MAY be invoked concurrently from multiple threads.

The implementation SHALL serialize state transitions.

---

# 12. Dependencies

The contract SHALL depend only on:

- Domain Model;
- IService.

The contract SHALL NOT depend on GUI widgets or multimedia frameworks.

---

# 13. AI Implementation Rules

Implementations SHALL:

- separate playback control from decoding;
- never modify Domain objects;
- expose playback state through immutable read models;
- publish playback events asynchronously.

---

# 14. Test Requirements

Tests SHALL verify:

- play;
- pause;
- stop;
- seek;
- navigation;
- speed control;
- loop mode;
- concurrent control requests.

---

# 15. Compliance Checklist

An implementation conforms to IPlaybackService only if it:

- provides transport control;
- provides playback state management;
- supports timeline navigation;
- does not modify the Domain Model;
- remains independent of multimedia backend.

---

End of Document