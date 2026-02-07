from datetime import datetime

date_string = datetime.now().strftime("%Y%m%d_%H%M%S")
resolve = app.GetResolve()

projectManager = resolve.GetProjectManager()
project = projectManager.GetCurrentProject()
current_timeline = project.GetCurrentTimeline()

mediaPool = project.GetMediaPool()
rootFolder = mediaPool.GetRootFolder()
subFolders = rootFolder.GetSubFolders() 

""" DaVinci Resolve auto switches to a new timeline - for this reason,
I decided to give the new timeline the old name, original_tl, and the new one the new name,
or as I called it, security_tl. So technically, after making a security copy, you're working
with the new copy - but that is, of course, completely without importance to the user. """

original_tl = current_timeline.GetName()
security_tl = "%s_%s" % (date_string, original_tl)

current_timeline.SetName(security_tl)
current_timeline.DuplicateTimeline(original_tl)

print("Done - new timeline '%s' created!" % security_tl)
print("You're now in %s" % original_tl)