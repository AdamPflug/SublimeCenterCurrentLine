import sublime_plugin
import sublime


class CenterCurrentLineCommand(sublime_plugin.TextCommand):
    def __init__(self, view):
        self.view = view
        settings = sublime.load_settings('Default.sublime-settings')
        view.settings().set('center_current_line', settings.get('center_current_line',  True))

    def run(self, args):
        sel = self.view.sel()
        if len(sel) == 1 and self.view.settings().get('center_current_line'):
            self.view.show_at_center(sel[0])


class CenterCurrentLineOnCommand(sublime_plugin.TextCommand):
    def __init__(self, view):
        self.view = view

    def run(self, args):
        self.view.settings().set('center_current_line', True)


class CenterCurrentLineOffCommand(sublime_plugin.TextCommand):
    def __init__(self, view):
        self.view = view

    def run(self, args):
        self.view.settings().set('center_current_line', False)


class CenterLineEventHandler(sublime_plugin.EventListener):
    def on_selection_modified(self, view):
        view.run_command('center_current_line')
