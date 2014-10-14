from . import View
from tracer.resources.lang import _
from tracer.views.note_for_hidden import NoteForHiddenView


class InteractiveView(View):
	def render(self):
		if self.args.processes:
			print _("you_should_restart")

		i = 1
		digits = len(str(len(self.args.processes)))
		for process in self.args.processes:
			n = "[{0}]".format(i).ljust(digits + 2)
			print "{} {}".format(n, process.name)
			i += 1

		if not self.args.args.all:
			if self.args.processes and (self.args.session_count or self.args.static_count):
				print ""

			view = NoteForHiddenView()
			view.assign("args", self.args.args)
			view.assign("total_count", self.args.total_count)
			view.assign("session_count", self.args.session_count)
			view.assign("static_count", self.args.static_count)
			view.render()

