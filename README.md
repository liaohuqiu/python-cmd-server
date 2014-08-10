###installation

```bash
$ pip install cmd-server
```

###start service

```bash
$ cubi-cmd-server
```

###php client

```php
$cmd = "git pull";

$end_point = 'cmd@tcp:127.0.0.1:2017';
$proxy = MCore_Proxy_CubeProxy::getInstance($end_point);
$data = array();
$data['cmd'] = $cmd;
$ret = $proxy->request('run', $data);
```

###python client

```python
#! /usr/bin/env python
import gevent.monkey
gevent.monkey.patch_all()
import cubi.proxy as proxy
import cubi.logger as logger

if __name__ == '__main__':
    logger.enable_debug_log()
    endp = 'cmd@tcp::2017'
    print 'start test for ', endp
    prx = proxy.Proxy(endp, True)

    data = {'cmd': 'ls -l'}
    r = prx.request('run', data)
    print r['data']
```
