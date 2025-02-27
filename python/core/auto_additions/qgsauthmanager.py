# The following has been generated automatically from src/core/auth/qgsauthmanager.h
QgsAuthManager.MessageLevel.baseClass = QgsAuthManager
try:
    QgsAuthManager.__attribute_docs__ = {'AUTH_PASSWORD_HELPER_DISPLAY_NAME': 'The display name of the password helper (platform dependent)', 'AUTH_MAN_TAG': 'The display name of the Authentication Manager', 'passwordHelperFailure': 'Signals emitted on password helper failure,\nmainly used in the tests to exit main application loop\n', 'passwordHelperSuccess': 'Signals emitted on password helper success,\nmainly used in the tests to exit main application loop\n', 'messageOut': 'Custom logging signal to relay to console output and :py:class:`QgsMessageLog`\n\n:param message: Message to send\n:param tag: Associated tag (title)\n:param level: Message log level\n\n.. seealso:: :py:class:`QgsMessageLog`\n', 'passwordHelperMessageOut': 'Custom logging signal to inform the user about master password <-> password manager interactions\n\n:param message: Message to send\n:param tag: Associated tag (title)\n:param level: Message log level\n\n.. seealso:: :py:class:`QgsMessageLog`\n', 'masterPasswordVerified': "Emitted when a password has been verify (or not)\n\n:param verified: The state of password's verification\n", 'authDatabaseEraseRequested': 'Emitted when a user has indicated they may want to erase the authentication db.\n', 'authDatabaseChanged': 'Emitted when the authentication db is significantly changed, e.g. large record removal, erased, etc.\n'}
except NameError:
    pass
QgsAuthManager.hasConfigId = staticmethod(QgsAuthManager.hasConfigId)
QgsAuthManager.passwordHelperEnabled = staticmethod(QgsAuthManager.passwordHelperEnabled)
try:
    QgsAuthManager.__group__ = ['auth']
except NameError:
    pass
