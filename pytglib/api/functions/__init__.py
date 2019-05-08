from .get_authorization_state import GetAuthorizationState
from .set_tdlib_parameters import SetTdlibParameters
from .check_database_encryption_key import CheckDatabaseEncryptionKey
from .set_authentication_phone_number import SetAuthenticationPhoneNumber
from .resend_authentication_code import ResendAuthenticationCode
from .check_authentication_code import CheckAuthenticationCode
from .check_authentication_password import CheckAuthenticationPassword
from .request_authentication_password_recovery import RequestAuthenticationPasswordRecovery
from .recover_authentication_password import RecoverAuthenticationPassword
from .check_authentication_bot_token import CheckAuthenticationBotToken
from .log_out import LogOut
from .close import Close
from .destroy import Destroy
from .get_current_state import GetCurrentState
from .set_database_encryption_key import SetDatabaseEncryptionKey
from .get_password_state import GetPasswordState
from .set_password import SetPassword
from .get_recovery_email_address import GetRecoveryEmailAddress
from .set_recovery_email_address import SetRecoveryEmailAddress
from .check_recovery_email_address_code import CheckRecoveryEmailAddressCode
from .resend_recovery_email_address_code import ResendRecoveryEmailAddressCode
from .request_password_recovery import RequestPasswordRecovery
from .recover_password import RecoverPassword
from .create_temporary_password import CreateTemporaryPassword
from .get_temporary_password_state import GetTemporaryPasswordState
from .get_me import GetMe
from .get_user import GetUser
from .get_user_full_info import GetUserFullInfo
from .get_basic_group import GetBasicGroup
from .get_basic_group_full_info import GetBasicGroupFullInfo
from .get_supergroup import GetSupergroup
from .get_supergroup_full_info import GetSupergroupFullInfo
from .get_secret_chat import GetSecretChat
from .get_chat import GetChat
from .get_message import GetMessage
from .get_message_locally import GetMessageLocally
from .get_replied_message import GetRepliedMessage
from .get_chat_pinned_message import GetChatPinnedMessage
from .get_messages import GetMessages
from .get_file import GetFile
from .get_remote_file import GetRemoteFile
from .get_chats import GetChats
from .search_public_chat import SearchPublicChat
from .search_public_chats import SearchPublicChats
from .search_chats import SearchChats
from .search_chats_on_server import SearchChatsOnServer
from .get_top_chats import GetTopChats
from .remove_top_chat import RemoveTopChat
from .add_recently_found_chat import AddRecentlyFoundChat
from .remove_recently_found_chat import RemoveRecentlyFoundChat
from .clear_recently_found_chats import ClearRecentlyFoundChats
from .check_chat_username import CheckChatUsername
from .get_created_public_chats import GetCreatedPublicChats
from .get_groups_in_common import GetGroupsInCommon
from .get_chat_history import GetChatHistory
from .delete_chat_history import DeleteChatHistory
from .search_chat_messages import SearchChatMessages
from .search_messages import SearchMessages
from .search_secret_messages import SearchSecretMessages
from .search_call_messages import SearchCallMessages
from .search_chat_recent_location_messages import SearchChatRecentLocationMessages
from .get_active_live_location_messages import GetActiveLiveLocationMessages
from .get_chat_message_by_date import GetChatMessageByDate
from .get_chat_message_count import GetChatMessageCount
from .remove_notification import RemoveNotification
from .remove_notification_group import RemoveNotificationGroup
from .get_public_message_link import GetPublicMessageLink
from .get_message_link import GetMessageLink
from .send_message import SendMessage
from .send_message_album import SendMessageAlbum
from .send_bot_start_message import SendBotStartMessage
from .send_inline_query_result_message import SendInlineQueryResultMessage
from .forward_messages import ForwardMessages
from .send_chat_set_ttl_message import SendChatSetTtlMessage
from .send_chat_screenshot_taken_notification import SendChatScreenshotTakenNotification
from .add_local_message import AddLocalMessage
from .delete_messages import DeleteMessages
from .delete_chat_messages_from_user import DeleteChatMessagesFromUser
from .edit_message_text import EditMessageText
from .edit_message_live_location import EditMessageLiveLocation
from .edit_message_media import EditMessageMedia
from .edit_message_caption import EditMessageCaption
from .edit_message_reply_markup import EditMessageReplyMarkup
from .edit_inline_message_text import EditInlineMessageText
from .edit_inline_message_live_location import EditInlineMessageLiveLocation
from .edit_inline_message_media import EditInlineMessageMedia
from .edit_inline_message_caption import EditInlineMessageCaption
from .edit_inline_message_reply_markup import EditInlineMessageReplyMarkup
from .get_text_entities import GetTextEntities
from .parse_text_entities import ParseTextEntities
from .get_file_mime_type import GetFileMimeType
from .get_file_extension import GetFileExtension
from .clean_file_name import CleanFileName
from .get_language_pack_string import GetLanguagePackString
from .get_json_value import GetJsonValue
from .get_json_string import GetJsonString
from .set_poll_answer import SetPollAnswer
from .stop_poll import StopPoll
from .get_inline_query_results import GetInlineQueryResults
from .answer_inline_query import AnswerInlineQuery
from .get_callback_query_answer import GetCallbackQueryAnswer
from .answer_callback_query import AnswerCallbackQuery
from .answer_shipping_query import AnswerShippingQuery
from .answer_pre_checkout_query import AnswerPreCheckoutQuery
from .set_game_score import SetGameScore
from .set_inline_game_score import SetInlineGameScore
from .get_game_high_scores import GetGameHighScores
from .get_inline_game_high_scores import GetInlineGameHighScores
from .delete_chat_reply_markup import DeleteChatReplyMarkup
from .send_chat_action import SendChatAction
from .open_chat import OpenChat
from .close_chat import CloseChat
from .view_messages import ViewMessages
from .open_message_content import OpenMessageContent
from .read_all_chat_mentions import ReadAllChatMentions
from .create_private_chat import CreatePrivateChat
from .create_basic_group_chat import CreateBasicGroupChat
from .create_supergroup_chat import CreateSupergroupChat
from .create_secret_chat import CreateSecretChat
from .create_new_basic_group_chat import CreateNewBasicGroupChat
from .create_new_supergroup_chat import CreateNewSupergroupChat
from .create_new_secret_chat import CreateNewSecretChat
from .upgrade_basic_group_chat_to_supergroup_chat import UpgradeBasicGroupChatToSupergroupChat
from .set_chat_title import SetChatTitle
from .set_chat_photo import SetChatPhoto
from .set_chat_draft_message import SetChatDraftMessage
from .set_chat_notification_settings import SetChatNotificationSettings
from .toggle_chat_is_pinned import ToggleChatIsPinned
from .toggle_chat_is_marked_as_unread import ToggleChatIsMarkedAsUnread
from .toggle_chat_default_disable_notification import ToggleChatDefaultDisableNotification
from .set_chat_client_data import SetChatClientData
from .pin_chat_message import PinChatMessage
from .unpin_chat_message import UnpinChatMessage
from .join_chat import JoinChat
from .leave_chat import LeaveChat
from .add_chat_member import AddChatMember
from .add_chat_members import AddChatMembers
from .set_chat_member_status import SetChatMemberStatus
from .get_chat_member import GetChatMember
from .search_chat_members import SearchChatMembers
from .get_chat_administrators import GetChatAdministrators
from .clear_all_draft_messages import ClearAllDraftMessages
from .get_chat_notification_settings_exceptions import GetChatNotificationSettingsExceptions
from .get_scope_notification_settings import GetScopeNotificationSettings
from .set_scope_notification_settings import SetScopeNotificationSettings
from .reset_all_notification_settings import ResetAllNotificationSettings
from .set_pinned_chats import SetPinnedChats
from .download_file import DownloadFile
from .get_file_downloaded_prefix_size import GetFileDownloadedPrefixSize
from .cancel_download_file import CancelDownloadFile
from .upload_file import UploadFile
from .cancel_upload_file import CancelUploadFile
from .write_generated_file_part import WriteGeneratedFilePart
from .set_file_generation_progress import SetFileGenerationProgress
from .finish_file_generation import FinishFileGeneration
from .read_file_part import ReadFilePart
from .delete_file import DeleteFile
from .generate_chat_invite_link import GenerateChatInviteLink
from .check_chat_invite_link import CheckChatInviteLink
from .join_chat_by_invite_link import JoinChatByInviteLink
from .create_call import CreateCall
from .accept_call import AcceptCall
from .discard_call import DiscardCall
from .send_call_rating import SendCallRating
from .send_call_debug_information import SendCallDebugInformation
from .block_user import BlockUser
from .unblock_user import UnblockUser
from .get_blocked_users import GetBlockedUsers
from .import_contacts import ImportContacts
from .get_contacts import GetContacts
from .search_contacts import SearchContacts
from .remove_contacts import RemoveContacts
from .get_imported_contact_count import GetImportedContactCount
from .change_imported_contacts import ChangeImportedContacts
from .clear_imported_contacts import ClearImportedContacts
from .get_user_profile_photos import GetUserProfilePhotos
from .get_stickers import GetStickers
from .search_stickers import SearchStickers
from .get_installed_sticker_sets import GetInstalledStickerSets
from .get_archived_sticker_sets import GetArchivedStickerSets
from .get_trending_sticker_sets import GetTrendingStickerSets
from .get_attached_sticker_sets import GetAttachedStickerSets
from .get_sticker_set import GetStickerSet
from .search_sticker_set import SearchStickerSet
from .search_installed_sticker_sets import SearchInstalledStickerSets
from .search_sticker_sets import SearchStickerSets
from .change_sticker_set import ChangeStickerSet
from .view_trending_sticker_sets import ViewTrendingStickerSets
from .reorder_installed_sticker_sets import ReorderInstalledStickerSets
from .get_recent_stickers import GetRecentStickers
from .add_recent_sticker import AddRecentSticker
from .remove_recent_sticker import RemoveRecentSticker
from .clear_recent_stickers import ClearRecentStickers
from .get_favorite_stickers import GetFavoriteStickers
from .add_favorite_sticker import AddFavoriteSticker
from .remove_favorite_sticker import RemoveFavoriteSticker
from .get_sticker_emojis import GetStickerEmojis
from .get_saved_animations import GetSavedAnimations
from .add_saved_animation import AddSavedAnimation
from .remove_saved_animation import RemoveSavedAnimation
from .get_recent_inline_bots import GetRecentInlineBots
from .search_hashtags import SearchHashtags
from .remove_recent_hashtag import RemoveRecentHashtag
from .get_web_page_preview import GetWebPagePreview
from .get_web_page_instant_view import GetWebPageInstantView
from .set_profile_photo import SetProfilePhoto
from .delete_profile_photo import DeleteProfilePhoto
from .set_name import SetName
from .set_bio import SetBio
from .set_username import SetUsername
from .change_phone_number import ChangePhoneNumber
from .resend_change_phone_number_code import ResendChangePhoneNumberCode
from .check_change_phone_number_code import CheckChangePhoneNumberCode
from .get_active_sessions import GetActiveSessions
from .terminate_session import TerminateSession
from .terminate_all_other_sessions import TerminateAllOtherSessions
from .get_connected_websites import GetConnectedWebsites
from .disconnect_website import DisconnectWebsite
from .disconnect_all_websites import DisconnectAllWebsites
from .toggle_basic_group_administrators import ToggleBasicGroupAdministrators
from .set_supergroup_username import SetSupergroupUsername
from .set_supergroup_sticker_set import SetSupergroupStickerSet
from .toggle_supergroup_invites import ToggleSupergroupInvites
from .toggle_supergroup_sign_messages import ToggleSupergroupSignMessages
from .toggle_supergroup_is_all_history_available import ToggleSupergroupIsAllHistoryAvailable
from .set_supergroup_description import SetSupergroupDescription
from .report_supergroup_spam import ReportSupergroupSpam
from .get_supergroup_members import GetSupergroupMembers
from .delete_supergroup import DeleteSupergroup
from .close_secret_chat import CloseSecretChat
from .get_chat_event_log import GetChatEventLog
from .get_payment_form import GetPaymentForm
from .validate_order_info import ValidateOrderInfo
from .send_payment_form import SendPaymentForm
from .get_payment_receipt import GetPaymentReceipt
from .get_saved_order_info import GetSavedOrderInfo
from .delete_saved_order_info import DeleteSavedOrderInfo
from .delete_saved_credentials import DeleteSavedCredentials
from .get_support_user import GetSupportUser
from .get_wallpapers import GetWallpapers
from .get_localization_target_info import GetLocalizationTargetInfo
from .get_language_pack_info import GetLanguagePackInfo
from .get_language_pack_strings import GetLanguagePackStrings
from .synchronize_language_pack import SynchronizeLanguagePack
from .add_custom_server_language_pack import AddCustomServerLanguagePack
from .set_custom_language_pack import SetCustomLanguagePack
from .edit_custom_language_pack_info import EditCustomLanguagePackInfo
from .set_custom_language_pack_string import SetCustomLanguagePackString
from .delete_language_pack import DeleteLanguagePack
from .register_device import RegisterDevice
from .process_push_notification import ProcessPushNotification
from .get_push_receiver_id import GetPushReceiverId
from .get_recently_visited_t_me_urls import GetRecentlyVisitedTMeUrls
from .set_user_privacy_setting_rules import SetUserPrivacySettingRules
from .get_user_privacy_setting_rules import GetUserPrivacySettingRules
from .get_option import GetOption
from .set_option import SetOption
from .set_account_ttl import SetAccountTtl
from .get_account_ttl import GetAccountTtl
from .delete_account import DeleteAccount
from .get_chat_report_spam_state import GetChatReportSpamState
from .change_chat_report_spam_state import ChangeChatReportSpamState
from .report_chat import ReportChat
from .get_chat_statistics_url import GetChatStatisticsUrl
from .get_storage_statistics import GetStorageStatistics
from .get_storage_statistics_fast import GetStorageStatisticsFast
from .get_database_statistics import GetDatabaseStatistics
from .optimize_storage import OptimizeStorage
from .set_network_type import SetNetworkType
from .get_network_statistics import GetNetworkStatistics
from .add_network_statistics import AddNetworkStatistics
from .reset_network_statistics import ResetNetworkStatistics
from .get_passport_element import GetPassportElement
from .get_all_passport_elements import GetAllPassportElements
from .set_passport_element import SetPassportElement
from .delete_passport_element import DeletePassportElement
from .set_passport_element_errors import SetPassportElementErrors
from .get_preferred_country_language import GetPreferredCountryLanguage
from .send_phone_number_verification_code import SendPhoneNumberVerificationCode
from .resend_phone_number_verification_code import ResendPhoneNumberVerificationCode
from .check_phone_number_verification_code import CheckPhoneNumberVerificationCode
from .send_email_address_verification_code import SendEmailAddressVerificationCode
from .resend_email_address_verification_code import ResendEmailAddressVerificationCode
from .check_email_address_verification_code import CheckEmailAddressVerificationCode
from .get_passport_authorization_form import GetPassportAuthorizationForm
from .get_passport_authorization_form_available_elements import GetPassportAuthorizationFormAvailableElements
from .send_passport_authorization_form import SendPassportAuthorizationForm
from .send_phone_number_confirmation_code import SendPhoneNumberConfirmationCode
from .resend_phone_number_confirmation_code import ResendPhoneNumberConfirmationCode
from .check_phone_number_confirmation_code import CheckPhoneNumberConfirmationCode
from .set_bot_updates_status import SetBotUpdatesStatus
from .upload_sticker_file import UploadStickerFile
from .create_new_sticker_set import CreateNewStickerSet
from .add_sticker_to_set import AddStickerToSet
from .set_sticker_position_in_set import SetStickerPositionInSet
from .remove_sticker_from_set import RemoveStickerFromSet
from .get_map_thumbnail_file import GetMapThumbnailFile
from .accept_terms_of_service import AcceptTermsOfService
from .send_custom_request import SendCustomRequest
from .answer_custom_query import AnswerCustomQuery
from .set_alarm import SetAlarm
from .get_country_code import GetCountryCode
from .get_invite_text import GetInviteText
from .get_deep_link_info import GetDeepLinkInfo
from .get_application_config import GetApplicationConfig
from .save_application_log_event import SaveApplicationLogEvent
from .add_proxy import AddProxy
from .edit_proxy import EditProxy
from .enable_proxy import EnableProxy
from .disable_proxy import DisableProxy
from .remove_proxy import RemoveProxy
from .get_proxies import GetProxies
from .get_proxy_link import GetProxyLink
from .ping_proxy import PingProxy
from .set_log_stream import SetLogStream
from .get_log_stream import GetLogStream
from .set_log_verbosity_level import SetLogVerbosityLevel
from .get_log_verbosity_level import GetLogVerbosityLevel
from .get_log_tags import GetLogTags
from .set_log_tag_verbosity_level import SetLogTagVerbosityLevel
from .get_log_tag_verbosity_level import GetLogTagVerbosityLevel
from .add_log_message import AddLogMessage
from .test_call_empty import TestCallEmpty
from .test_call_string import TestCallString
from .test_call_bytes import TestCallBytes
from .test_call_vector_int import TestCallVectorInt
from .test_call_vector_int_object import TestCallVectorIntObject
from .test_call_vector_string import TestCallVectorString
from .test_call_vector_string_object import TestCallVectorStringObject
from .test_square_int import TestSquareInt
from .test_network import TestNetwork
from .test_get_difference import TestGetDifference
from .test_use_update import TestUseUpdate
from .test_use_error import TestUseError
