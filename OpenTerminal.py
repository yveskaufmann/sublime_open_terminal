import sublime, sublime_plugin

# Load Plugin Settings
settings = {}
def plugin_loaded():
    global settings
    settings = sublime.load_settings('OpenTerminal.sublime-settings')

def window():
    return sublime.active_window()

def activeView():
    return window().active_view()



class OpenTerminalCommand(sublime_plugin.ApplicationCommand):
    def run(self):
        import subprocess
        if settings.get('use_powershell', False):
            subprocess.Popen(['start', 'powershell'], shell=True, cwd=self.currentPath())
        else:
            subprocess.Popen(['start', 'cmd'], shell=True, cwd=self.currentPath())
    
    def currentPath(self):
        import os
        activeFile = activeView().file_name()
        if activeFile is None: 
            folders = window().folders()
            if len(folders) > 0:
                return folders[0]
            else: 
                return '.'
        return os.path.dirname(activeFile)