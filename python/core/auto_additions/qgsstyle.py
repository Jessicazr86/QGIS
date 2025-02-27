# The following has been generated automatically from src/core/symbology/qgsstyle.h
# monkey patching scoped based enum
QgsStyle.TextFormatContext.Labeling.__doc__ = "Text format used in labeling"
QgsStyle.TextFormatContext.__doc__ = "Text format context.\n\n.. versionadded:: 3.20\n\n" + '* ``Labeling``: ' + QgsStyle.TextFormatContext.Labeling.__doc__
# --
try:
    QgsStyle.__attribute_docs__ = {'initialized': 'Emitted when the style database has been fully initialized.\n\nThis signals is only emitted by the :py:func:`QgsStyle.defaultStyle()` instance,\nand only when the :py:func:`~QgsStyle.defaultStyle` has been lazily initialized.\n\n.. versionadded:: 3.36\n', 'aboutToBeDestroyed': 'Emitted just before the style object is destroyed.\n\nEmitted in the destructor when the style is about to be deleted,\nbut it is still in a perfectly valid state: the last chance for\nother pieces of code for some cleanup if they use the style.\n\n.. versionadded:: 3.26\n', 'symbolSaved': 'Emitted every time a new symbol has been added to the database.\nEmitted whenever a symbol has been added to the style and the database\nhas been updated as a result.\n\n.. seealso:: :py:func:`symbolRemoved`\n\n.. seealso:: :py:func:`rampAdded`\n\n.. seealso:: :py:func:`symbolChanged`\n', 'symbolChanged': "Emitted whenever a symbol's definition is changed. This does not include\nname or tag changes.\n\n.. seealso:: :py:func:`symbolSaved`\n\n.. versionadded:: 3.4\n", 'groupsModified': 'Emitted every time a tag or smartgroup has been added, removed, or renamed\n', 'entityTagsChanged': "Emitted whenever an ``entity``'s tags are changed.\n\n.. versionadded:: 3.4\n", 'favoritedChanged': 'Emitted whenever an ``entity`` is either favorited or un-favorited.\n\n.. versionadded:: 3.4\n', 'entityAdded': 'Emitted every time a new entity has been added to the database.\n\n.. versionadded:: 3.14\n', 'entityRemoved': 'Emitted whenever an entity of the specified type is removed from the style and the database\nhas been updated as a result.\n\n.. versionadded:: 3.14\n', 'entityRenamed': 'Emitted whenever a entity of the specified type has been renamed from ``oldName`` to ``newName``\n\n.. versionadded:: 3.14\n', 'entityChanged': "Emitted whenever an entity's definition is changed. This does not include\nname or tag changes.\n\n.. versionadded:: 3.14\n", 'symbolRemoved': 'Emitted whenever a symbol has been removed from the style and the database\nhas been updated as a result.\n\n.. seealso:: :py:func:`symbolSaved`\n\n.. seealso:: :py:func:`rampRemoved`\n\n.. versionadded:: 3.4\n', 'symbolRenamed': 'Emitted whenever a symbol has been renamed from ``oldName`` to ``newName``\n\n.. seealso:: :py:func:`rampRenamed`\n\n.. versionadded:: 3.4\n', 'rampRenamed': 'Emitted whenever a color ramp has been renamed from ``oldName`` to ``newName``\n\n.. seealso:: :py:func:`symbolRenamed`\n\n.. versionadded:: 3.4\n', 'rampAdded': 'Emitted whenever a color ramp has been added to the style and the database\nhas been updated as a result.\n\n.. seealso:: :py:func:`rampRemoved`\n\n.. seealso:: :py:func:`symbolSaved`\n\n.. versionadded:: 3.4\n', 'rampRemoved': 'Emitted whenever a color ramp has been removed from the style and the database\nhas been updated as a result.\n\n.. seealso:: :py:func:`rampAdded`\n\n.. seealso:: :py:func:`symbolRemoved`\n\n.. versionadded:: 3.4\n', 'rampChanged': "Emitted whenever a color ramp's definition is changed. This does not include\nname or tag changes.\n\n.. seealso:: :py:func:`rampAdded`\n\n.. versionadded:: 3.4\n", 'textFormatRenamed': 'Emitted whenever a text format has been renamed from ``oldName`` to ``newName``\n\n.. seealso:: :py:func:`symbolRenamed`\n\n.. versionadded:: 3.10\n', 'textFormatAdded': 'Emitted whenever a text format has been added to the style and the database\nhas been updated as a result.\n\n.. seealso:: :py:func:`textFormatRemoved`\n\n.. seealso:: :py:func:`symbolSaved`\n\n.. versionadded:: 3.10\n', 'textFormatRemoved': 'Emitted whenever a text format has been removed from the style and the database\nhas been updated as a result.\n\n.. seealso:: :py:func:`textFormatAdded`\n\n.. seealso:: :py:func:`symbolRemoved`\n\n.. versionadded:: 3.10\n', 'textFormatChanged': "Emitted whenever a text format's definition is changed. This does not include\nname or tag changes.\n\n.. seealso:: :py:func:`textFormatAdded`\n\n.. versionadded:: 3.10\n", 'labelSettingsRenamed': 'Emitted whenever label settings have been renamed from ``oldName`` to ``newName``\n\n.. seealso:: :py:func:`symbolRenamed`\n\n.. versionadded:: 3.10\n', 'labelSettingsAdded': 'Emitted whenever label settings have been added to the style and the database\nhas been updated as a result.\n\n.. seealso:: :py:func:`labelSettingsRemoved`\n\n.. seealso:: :py:func:`symbolSaved`\n\n.. versionadded:: 3.10\n', 'labelSettingsRemoved': 'Emitted whenever label settings have been removed from the style and the database\nhas been updated as a result.\n\n.. seealso:: :py:func:`labelSettingsAdded`\n\n.. seealso:: :py:func:`symbolRemoved`\n\n.. versionadded:: 3.10\n', 'labelSettingsChanged': "Emitted whenever a label setting's definition is changed. This does not include\nname or tag changes.\n\n.. seealso:: :py:func:`labelSettingsAdded`\n\n.. versionadded:: 3.10\n", 'rebuildIconPreviews': 'Emitted whenever icon previews for entities in the style must be rebuilt.\n\n.. versionadded:: 3.26\n'}
except NameError:
    pass
QgsStyle.defaultStyle = staticmethod(QgsStyle.defaultStyle)
QgsStyle.defaultTextFormatForProject = staticmethod(QgsStyle.defaultTextFormatForProject)
QgsStyle.isXmlStyleFile = staticmethod(QgsStyle.isXmlStyleFile)
try:
    QgsStyle.__group__ = ['symbology']
except NameError:
    pass
try:
    QgsStyleEntityInterface.__group__ = ['symbology']
except NameError:
    pass
try:
    QgsStyleSymbolEntity.__group__ = ['symbology']
except NameError:
    pass
try:
    QgsStyleColorRampEntity.__group__ = ['symbology']
except NameError:
    pass
try:
    QgsStyleTextFormatEntity.__group__ = ['symbology']
except NameError:
    pass
try:
    QgsStyleLabelSettingsEntity.__group__ = ['symbology']
except NameError:
    pass
try:
    QgsStyleLegendPatchShapeEntity.__group__ = ['symbology']
except NameError:
    pass
try:
    QgsStyleSymbol3DEntity.__group__ = ['symbology']
except NameError:
    pass
