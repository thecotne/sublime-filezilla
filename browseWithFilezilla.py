import sublime_plugin, sublime, subprocess, os
from .dirConfig import getConfig

configName = 'sftp-config.json'

startFilezillaCommand = 'filezilla {type}://{user}:{password}@{host}:{port}"{remote_path}" --local="{local_path}"'

class browse_with_filezillaCommand(sublime_plugin.WindowCommand):
	def run(self, edit = None):
		conf = getConfig(configName)
		if conf is not None:
			subprocess.Popen(startFilezillaCommand.format(**conf), shell=True)

