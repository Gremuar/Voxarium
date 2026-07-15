# Voxarium Software Architecture Specification

Document Path:

spec/000_Foundation/Documentation_Index.md

Document ID:

FOUND-000

Title:

Documentation Index

Version:

1.0.0

Status:

Accepted

Classification:

Normative

---

# 1. Purpose

This document defines the complete set of architecture specification documents
that comprise the Voxarium Software Architecture Specification.

It is the authoritative index of every normative document in the repository.

Documents not listed in this index SHALL NOT be considered part of the official architecture.

All future documents SHALL first be added to this index before being created.

---

# 2. Repository Structure

```
spec/
├── 000_Foundation/
├── 100_Domain/
├── 200_Application/
├── 300_Contracts/
├── 400_Commands/
├── 500_Events/
├── 600_Project_Format/
├── 700_Plugins/
├── 800_GUI/
├── 900_Testing/
└── 999_ADR/
```

---

# 3. Documentation Rules

Every document SHALL:

- belong to exactly one section;
- have a unique filename;
- have a unique Document ID;
- appear exactly once in this index.

Documents SHALL be organized alphabetically inside each section.

---

# 4. Documentation Tree

---

# 000_Foundation

Architecture_Principles.md

Architecture_Overview.md

Bounded_Contexts.md

Coding_Standards.md

Component_Model.md

Dependency_Rules.md

Documentation_Index.md

Error_Model.md

Event_Model.md

Glossary.md

Layered_Architecture.md

Naming_Conventions.md

Repository_Structure.md

System_Context.md

Terminology.md

---

# 100_Domain

AudioAsset.md

AudioFragment.md

AudioGenerationJob.md

AudioGenerationPreset.md

AudioProfile.md

AudioSegment.md

Bookmark.md

Chapter.md

Character.md

Collection.md

Cue.md

Dictionary.md

DictionaryEntry.md

Document.md

DocumentMetadata.md

DocumentStatistics.md

EmotionPreset.md

ExportJob.md

Folder.md

Fragment.md

FragmentGroup.md

GenerationHistory.md

GenerationPreset.md

ImportJob.md

Language.md

Lexicon.md

LexiconEntry.md

Marker.md

Metadata.md

Note.md

PhonemeRule.md

PlaybackProfile.md

PluginReference.md

Project.md

ProjectMetadata.md

ProjectSettings.md

PronunciationDictionary.md

Role.md

Scene.md

Speaker.md

StylePreset.md

Subtitle.md

Tag.md

Task.md

TextAsset.md

Timeline.md

TimelineClip.md

TimelineMarker.md

TimelineTrack.md

TimelineTrackGroup.md

ValidationIssue.md

ValidationJob.md

ValidationRule.md

Voice.md

VoiceModel.md

VoicePreset.md

VoiceProfile.md

VoiceStyle.md

Waveform.md

Workspace.md

---

# 200_Application

ApplicationContext.md

ApplicationService.md

AssetManagementService.md

AudioExportService.md

AudioGenerationService.md

AudioImportService.md

AudioPlaybackService.md

AudioProcessingService.md

AudioQueueService.md

AudioRenderingService.md

AutoSaveService.md

BackupService.md

CacheService.md

ClipboardService.md

CollectionService.md

CommandBus.md

CommandHandler.md

ConfigurationService.md

DictionaryService.md

DocumentAnalysisService.md

DocumentService.md

EventBus.md

ExportService.md

FileStorageService.md

GenerationQueueService.md

GenerationScheduler.md

GenerationService.md

HistoryService.md

ImportService.md

IndexService.md

JobManager.md

JobScheduler.md

LanguageDetectionService.md

LicenseService.md

LoggingService.md

MetadataService.md

NotificationService.md

PluginDiscoveryService.md

PluginHostService.md

PluginManager.md

PreferenceService.md

PreviewService.md

ProjectService.md

QueueManager.md

RecentProjectsService.md

RecoveryService.md

RepositoryFactory.md

ResourceService.md

RoleAssignmentService.md

SearchIndexService.md

SearchService.md

SettingsService.md

SpeechSynthesisService.md

StatisticsService.md

StorageService.md

TaskScheduler.md

TelemetryService.md

TemplateService.md

TextAnalysisService.md

TextNormalizationService.md

ThemeService.md

TimelineEditingService.md

TimelinePlaybackService.md

TimelineService.md

TransactionManager.md

UndoRedoService.md

UpdateService.md

ValidationService.md

VoiceAssignmentService.md

VoiceModelService.md

VoicePreviewService.md

VoiceProfileService.md

VoiceSelectionService.md

WorkspaceService.md

---

# 300_Contracts

AnalysisResult.md

ApplicationConfiguration.md

ApplicationInfo.md

AudioAssetDto.md

AudioExportOptions.md

AudioGenerationOptions.md

AudioGenerationRequest.md

AudioGenerationResponse.md

AudioImportOptions.md

AudioMetadata.md

AudioPreviewRequest.md

AudioPreviewResponse.md

BackupOptions.md

BookmarkDto.md

CollectionDto.md

CommandResult.md

DictionaryDto.md

DocumentAnalysisResult.md

DocumentCreateRequest.md

DocumentDto.md

DocumentImportRequest.md

DocumentStatisticsDto.md

DocumentUpdateRequest.md

ErrorDetails.md

EventEnvelope.md

ExportOptions.md

ExportResult.md

FileDescriptor.md

FragmentCreateRequest.md

FragmentDto.md

FragmentUpdateRequest.md

GenerationJobDto.md

GenerationPresetDto.md

GenerationProgress.md

HealthCheckResult.md

ImportOptions.md

ImportResult.md

JobDto.md

JobProgress.md

LanguageDto.md

LexiconDto.md

LicenseInfo.md

MarkerDto.md

MetadataDto.md

NotificationDto.md

PageResult.md

PlaybackOptions.md

PluginCapability.md

PluginDescriptor.md

PluginInformation.md

PreviewResult.md

ProjectCreateRequest.md

ProjectDto.md

ProjectImportRequest.md

ProjectMetadataDto.md

ProjectOpenRequest.md

ProjectStatisticsDto.md

ProjectUpdateRequest.md

QueueItemDto.md

RoleDto.md

SearchQuery.md

SearchResult.md

SettingsDto.md

SpeakerDto.md

StatisticsDto.md

SubtitleDto.md

TagDto.md

TaskDto.md

TimelineClipDto.md

TimelineDto.md

TimelineMarkerDto.md

TimelineTrackDto.md

ValidationIssueDto.md

ValidationReport.md

VoiceDto.md

VoiceModelDto.md

VoicePresetDto.md

VoiceProfileDto.md

WorkspaceDto.md

---

# 400_Commands

AnalyzeDuplicateContentCommand.md

AnalyzeLanguageCommand.md

AnalyzeReadabilityCommand.md

AnalyzeSentimentCommand.md

AnalyzeTextStructureCommand.md

ArchiveProjectCommand.md

AssignRoleCommand.md

AssignVoiceProfileCommand.md

BackupProjectCommand.md

CancelAudioGenerationCommand.md

CancelJobCommand.md

CleanupProjectCommand.md

ClearCacheCommand.md

CloneDocumentCommand.md

CloneProjectCommand.md

CloseProjectCommand.md

ConvertDocumentCommand.md

CreateBookmarkCommand.md

CreateCollectionCommand.md

CreateDictionaryCommand.md

CreateDocumentCommand.md

CreateFragmentCommand.md

CreateGenerationPresetCommand.md

CreateMarkerCommand.md

CreateProjectCommand.md

CreateRoleCommand.md

CreateSpeakerCommand.md

CreateTagCommand.md

CreateTimelineCommand.md

CreateTimelineTrackCommand.md

CreateVoiceProfileCommand.md

DeleteBookmarkCommand.md

DeleteCollectionCommand.md

DeleteDictionaryCommand.md

DeleteDocumentCommand.md

DeleteFragmentCommand.md

DeleteGenerationPresetCommand.md

DeleteMarkerCommand.md

DeleteProjectCommand.md

DeleteRoleCommand.md

DeleteSpeakerCommand.md

DeleteTagCommand.md

DeleteTimelineCommand.md

DeleteTimelineTrackCommand.md

DeleteVoiceProfileCommand.md

DowngradeProjectCommand.md

DuplicateDocumentCommand.md

DuplicateFragmentCommand.md

DuplicateProjectCommand.md

ExportProjectCommand.md

GenerateAudioCommand.md

ImportProjectCommand.md

MergeDocumentsCommand.md

MergeFragmentsCommand.md

MigrateProjectCommand.md

MoveFragmentCommand.md

OpenProjectCommand.md

OptimizeProjectCommand.md

RebuildProjectIndexCommand.md

RenameProjectCommand.md

RepairProjectCommand.md

ResetProjectCommand.md

RestoreProjectCommand.md

SaveProjectAsCommand.md

SaveProjectCommand.md

SplitDocumentCommand.md

SplitFragmentCommand.md

UnarchiveProjectCommand.md

UpdateBookmarkCommand.md

UpdateCollectionCommand.md

UpdateDictionaryCommand.md

UpdateDocumentCommand.md

UpdateFragmentCommand.md

UpdateGenerationPresetCommand.md

UpdateMarkerCommand.md

UpdateProjectCommand.md

UpdateRoleCommand.md

UpdateSpeakerCommand.md

UpdateTagCommand.md

UpdateTimelineCommand.md

UpdateTimelineTrackCommand.md

UpdateVoiceProfileCommand.md

UpgradeProjectCommand.md

ValidateProjectCommand.md

---

# 500_Events

ApplicationClosingEvent.md

ApplicationOpenedEvent.md

ApplicationReadyEvent.md

ApplicationSettingsChangedEvent.md

ApplicationShutdownEvent.md

ArchiveCompletedEvent.md

ArchiveFailedEvent.md

ArchiveStartedEvent.md

AudioExportCompletedEvent.md

AudioExportFailedEvent.md

AudioExportStartedEvent.md

AudioGenerationCancelledEvent.md

AudioGenerationCompletedEvent.md

AudioGenerationFailedEvent.md

AudioGenerationPausedEvent.md

AudioGenerationProgressEvent.md

AudioGenerationQueuedEvent.md

AudioGenerationResumedEvent.md

AudioGenerationStartedEvent.md

AudioImportedEvent.md

AudioPlaybackFinishedEvent.md

AudioPlaybackPausedEvent.md

AudioPlaybackStartedEvent.md

AudioPlaybackStoppedEvent.md

BackupCompletedEvent.md

BackupFailedEvent.md

BackupStartedEvent.md

BookmarkCreatedEvent.md

BookmarkDeletedEvent.md

BookmarkUpdatedEvent.md

CacheClearedEvent.md

CollectionCreatedEvent.md

CollectionDeletedEvent.md

CollectionUpdatedEvent.md

CommandCompletedEvent.md

CommandFailedEvent.md

CommandStartedEvent.md

ConfigurationChangedEvent.md

DictionaryCreatedEvent.md

DictionaryDeletedEvent.md

DictionaryImportedEvent.md

DictionaryUpdatedEvent.md

DocumentAnalysisCompletedEvent.md

DocumentAnalysisFailedEvent.md

DocumentAnalysisStartedEvent.md

DocumentClosedEvent.md

DocumentConvertedEvent.md

DocumentCreatedEvent.md

DocumentDeletedEvent.md

DocumentExportedEvent.md

DocumentImportedEvent.md

DocumentOpenedEvent.md

DocumentRenamedEvent.md

DocumentSavedEvent.md

DocumentSplitEvent.md

DocumentUpdatedEvent.md

FragmentCreatedEvent.md

FragmentDeletedEvent.md

FragmentMergedEvent.md

FragmentMovedEvent.md

FragmentSplitEvent.md

FragmentUpdatedEvent.md

GenerationPresetCreatedEvent.md

GenerationPresetDeletedEvent.md

GenerationPresetUpdatedEvent.md

IndexRebuiltEvent.md

JobCancelledEvent.md

JobCompletedEvent.md

JobCreatedEvent.md

JobFailedEvent.md

JobPausedEvent.md

JobProgressChangedEvent.md

JobQueuedEvent.md

JobResumedEvent.md

JobStartedEvent.md

LanguageDetectedEvent.md

LicenseChangedEvent.md

MarkerCreatedEvent.md

MarkerDeletedEvent.md

MarkerUpdatedEvent.md

NotificationPublishedEvent.md

PluginDisabledEvent.md

PluginEnabledEvent.md

PluginInstalledEvent.md

PluginLoadedEvent.md

PluginUninstalledEvent.md

PluginUnloadedEvent.md

ProjectArchivedEvent.md

ProjectBackupCreatedEvent.md

ProjectClosedEvent.md

ProjectCreatedEvent.md

ProjectDeletedEvent.md

ProjectImportedEvent.md

ProjectLoadedEvent.md

ProjectMigratedEvent.md

ProjectOpenedEvent.md

ProjectOptimizedEvent.md

ProjectRenamedEvent.md

ProjectResetEvent.md

ProjectRestoredEvent.md

ProjectSavedEvent.md

ProjectUnarchivedEvent.md

ProjectUpdatedEvent.md

ProjectValidatedEvent.md

RecoveryCompletedEvent.md

RecoveryStartedEvent.md

RoleAssignedEvent.md

RoleCreatedEvent.md

RoleDeletedEvent.md

RoleUpdatedEvent.md

SearchCompletedEvent.md

SearchStartedEvent.md

SpeakerCreatedEvent.md

SpeakerDeletedEvent.md

SpeakerUpdatedEvent.md

StatisticsUpdatedEvent.md

TagCreatedEvent.md

TagDeletedEvent.md

TagUpdatedEvent.md

TimelineClipCreatedEvent.md

TimelineClipDeletedEvent.md

TimelineClipMovedEvent.md

TimelineClipUpdatedEvent.md

TimelineCreatedEvent.md

TimelineDeletedEvent.md

TimelineMarkerCreatedEvent.md

TimelineMarkerDeletedEvent.md

TimelineMarkerUpdatedEvent.md

TimelineTrackCreatedEvent.md

TimelineTrackDeletedEvent.md

TimelineTrackUpdatedEvent.md

ValidationCompletedEvent.md

ValidationFailedEvent.md

ValidationStartedEvent.md

VoiceAssignedEvent.md

VoiceModelChangedEvent.md

VoicePreviewGeneratedEvent.md

VoiceProfileCreatedEvent.md

VoiceProfileDeletedEvent.md

VoiceProfileUpdatedEvent.md

WorkspaceClosedEvent.md

WorkspaceCreatedEvent.md

WorkspaceOpenedEvent.md

WorkspaceSavedEvent.md

---

# 600_Project_Format

AudioAssets.md

AudioCache.md

AudioPackage.md

AudioPackageFormat.md

Bookmarks.md

Collections.md

Compression.md

CustomMetadata.md

DictionaryFormat.md

EmbeddedResources.md

Encryption.md

ExportPackage.md

ExternalResources.md

FileIntegrity.md

FileVersioning.md

FolderStructure.md

Fragments.md

ImportPackage.md

Indexes.md

Manifest.md

MediaAssets.md

Metadata.md

MigrationRules.md

PackageLayout.md

PluginConfiguration.md

ProjectConfiguration.md

ProjectFile.md

ProjectManifest.md

ProjectSettings.md

RecoveryInformation.md

ResourceIdentifiers.md

RoleAssignments.md

SchemaEvolution.md

SearchIndex.md

Security.md

StorageLayout.md

SubtitleAssets.md

TemporaryFiles.md

TextAssets.md

TimelineFormat.md

TimelineSerialization.md

Validation.md

VersionCompatibility.md

VoiceAssignments.md

VoiceResources.md

WorkspaceConfiguration.md

---

# 700_Plugins

AudioExporterPlugin.md

AudioImporterPlugin.md

AuthenticationPlugin.md

CapabilityModel.md

CommandExtension.md

ConfigurationExtension.md

DependencyInjection.md

EventExtension.md

ExtensionDiscovery.md

ExtensionPoint.md

ExtensionRegistration.md

FileFormatPlugin.md

GenerationEnginePlugin.md

Lifecycle.md

PermissionModel.md

PluginAPI.md

PluginCompatibility.md

PluginConfiguration.md

PluginContext.md

PluginDescriptor.md

PluginDiscovery.md

PluginIsolation.md

PluginLifecycle.md

PluginLoader.md

PluginLogging.md

PluginManifest.md

PluginManager.md

PluginPackaging.md

PluginRegistry.md

PluginSandbox.md

PluginSecurity.md

PluginService.md

PluginSettings.md

PluginSigning.md

PluginStorage.md

PluginTesting.md

ResourceExtension.md

ScriptPlugin.md

SearchProviderPlugin.md

SpeechEnginePlugin.md

ThemePlugin.md

UIExtension.md

ValidationPlugin.md

Versioning.md

WorkspaceExtension.md

---

# 800_GUI

AboutDialog.md

ApplicationLayout.md

AudioEditor.md

AudioExportDialog.md

AudioGenerationPanel.md

AudioPlayer.md

AudioPreviewPanel.md

BookmarkPanel.md

CollectionExplorer.md

ColorScheme.md

CommandPalette.md

ConfirmationDialogs.md

ContextMenus.md

DictionaryEditor.md

Dialogs.md

DocumentEditor.md

DocumentExplorer.md

DragAndDrop.md

ErrorDialogs.md

FileDialogs.md

FilterPanel.md

FindReplaceDialog.md

FontManagement.md

GenerationHistoryPanel.md

GenerationPresetEditor.md

GlobalToolbar.md

Iconography.md

ImportWizard.md

KeyboardShortcuts.md

LicenseDialog.md

LogViewer.md

MainMenu.md

MainWindow.md

MarkerPanel.md

NavigationModel.md

NotificationCenter.md

PreferencesDialog.md

ProgressDialogs.md

ProjectDashboard.md

ProjectExplorer.md

PropertyInspector.md

RecentProjectsView.md

RoleEditor.md

SearchPanel.md

SettingsDialog.md

SpeakerEditor.md

SplashScreen.md

StatusBar.md

SubtitleEditor.md

TabManagement.md

TagEditor.md

ThemeManager.md

TimelineEditor.md

TimelineNavigator.md

TimelineToolbar.md

Toolbar.md

TreeViews.md

ValidationPanel.md

VoiceAssignmentPanel.md

VoiceModelManager.md

VoicePreviewPanel.md

VoiceProfileEditor.md

WelcomeScreen.md

WindowManagement.md

WorkspaceLayout.md

---

# 900_Testing

AcceptanceTesting.md

ArchitectureComplianceTesting.md

AudioGenerationTesting.md

BenchmarkTesting.md

CodeCoverage.md

CommandTesting.md

ComponentTesting.md

ConcurrencyTesting.md

ConfigurationTesting.md

ContractTesting.md

DataIntegrityTesting.md

EndToEndTesting.md

ErrorHandlingTesting.md

EventTesting.md

GUIAutomationTesting.md

IntegrationTesting.md

LoadTesting.md

MigrationTesting.md

MockingStrategy.md

PerformanceTesting.md

PluginCompatibilityTesting.md

PluginTesting.md

RegressionTesting.md

RepositoryTesting.md

ResilienceTesting.md

SecurityTesting.md

SnapshotTesting.md

StressTesting.md

SystemTesting.md

TestDataManagement.md

TestEnvironment.md

TestExecutionStrategy.md

TestFixtures.md

TestNamingConventions.md

TestReporting.md

TestStrategy.md

UIComponentTesting.md

UnitTesting.md

ValidationTesting.md

WorkspaceRecoveryTesting.md

---

# 999_ADR

ADR-001_ProjectVision.md

ADR-002_CleanArchitecture.md

ADR-003_DomainDrivenDesign.md

ADR-004_CQRS.md

ADR-005_EventDrivenArchitecture.md

ADR-006_CommandBus.md

ADR-007_EventBus.md

ADR-008_RepositoryPattern.md

ADR-009_ProjectStorageFormat.md

ADR-010_PluggableSpeechEngines.md

ADR-011_PluginArchitecture.md

ADR-012_AsynchronousJobExecution.md

ADR-013_TimelineArchitecture.md

ADR-014_VoiceProfileModel.md

ADR-015_ProjectVersioning.md

ADR-016_BackupStrategy.md

ADR-017_ValidationStrategy.md

ADR-018_SearchArchitecture.md

ADR-019_CachingStrategy.md

ADR-020_ErrorHandlingStrategy.md

ADR-021_LoggingStrategy.md

ADR-022_ConfigurationManagement.md

ADR-023_SecurityModel.md

ADR-024_PermissionsModel.md

ADR-025_Internationalization.md

ADR-026_ThemingArchitecture.md

ADR-027_TestingStrategy.md

ADR-028_ExtensibilityModel.md

ADR-029_DeploymentModel.md

ADR-030_FutureEvolution.md

---

# 5. Index Maintenance Rules

This document is the authoritative inventory of the Voxarium Software
Architecture Specification.

Every architecture document SHALL appear exactly once in this index.

No architecture document SHALL be created unless it has first been added to
this index.

Removing or renaming a document SHALL require updating this index.

Each document SHALL belong to exactly one section.

Document filenames SHALL be unique across the entire specification.

---

# 6. Compliance

The architecture specification SHALL be considered complete only when every
document listed in this index exists in the repository.

The Documentation Index SHALL be treated as the contractual scope of the
architecture documentation.

Changes to the documentation scope SHALL be performed by modifying this
document first.

---

End of Document