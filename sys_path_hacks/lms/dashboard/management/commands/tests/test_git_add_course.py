from sys_path_hacks.warn import warn_deprecated_import

warn_deprecated_import('lms.djangoapps', 'dashboard.management.commands.tests.test_git_add_course')

from lms.djangoapps.dashboard.management.commands.tests.test_git_add_course import *
