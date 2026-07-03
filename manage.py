"""
 * Copyright (c) KylinSoft  Co., Ltd. 2024.All rights reserved.
 * PilotGo-plugin licensed under the Mulan Permissive Software License, Version 2. 
 * See LICENSE file for more details.
 * Author: wangqingzheng <wangqingzheng@kylinos.cn>
 * Date: Fri Feb 23 14:13:28 2024 +0800
"""
#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys


def main():
    """Run administrative tasks."""
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'kytuningProject.settings')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)
    # 自定义启动定时监控任务
    import schedule
    from appStore.utils.constants import MONITOR_KOJIFILES_TIME
    from appStore.utils.timed_tasks import new_monitor_kojifiles, start_scheduler

    schedule.every(MONITOR_KOJIFILES_TIME).minutes.do(new_monitor_kojifiles)
    start_scheduler()


if __name__ == '__main__':
    main()