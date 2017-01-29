import pynotify as noti 
noti.init("notify");
head = "GET UP"
content = "meet me at 7pm"
notification = noti.Notification.new(
	head,
	content,
)
notification.show();