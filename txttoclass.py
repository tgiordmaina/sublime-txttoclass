import sublime, sublime_plugin


class TxttoclassCommand(sublime_plugin.TextCommand):

    def run(self,edit):
        selection = ''
        for region in self.view.sel():
            selection += self.view.substr(region)
        if selection != '':
        	name = ''
        	upper = True
        	for c in selection:
        		co = ord(c)
        		if (co >= ord('a') and co <= ord('z')) or (co >= ord('A') and co <= ord('Z')):
        			if upper is True:
        				name = name + c.upper()
        				upper = False
        			else:
        				name = name + c
        		else:
        			upper = True
        	self.view.replace(edit, region, name)
