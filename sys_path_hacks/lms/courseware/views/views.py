from sys_path_hacks.warn import warn_deprecated_import

warn_deprecated_import('lms.djangoapps', 'courseware.views.views')

from lms.djangoapps.courseware.views.views import *
