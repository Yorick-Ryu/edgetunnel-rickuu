"""Apply the deployment overlay without modifying vendored upstream source."""
from pathlib import Path
root = Path(__file__).resolve().parent.parent
s = (root / 'src/worker-vless.js').read_text()
def replace(old, new):
 global s
 assert s.count(old) == 1, 'Upstream changed; review the deployment overlay before deploying'
 s = s.replace(old, new)
replace("let userID = 'd342d11e-d424-4583-b36e-524ab1f0afa4';", "let userID = '';")
replace("if (!isValidUUID(userID)) {\n\tthrow new Error('uuid is not valid');\n}", '')
replace('userID = env.UUID || userID;', "userID = env.UUID;\n            if (!userID || !isValidUUID(userID)) return new Response('Unavailable', {status: 503});")
a=s.index('\t\t\t\tswitch (url.pathname) {')
b=s.index('\n\t\t\t} else {', a)
s=s[:a]+"                return new Response(url.pathname === '/healthz' ? 'ok' : 'Not found', {status: url.pathname === '/healthz' ? 200 : 404});"+s[b:]
(root / 'deploy').mkdir(exist_ok=True)
(root / 'deploy/worker.js').write_text(s)
print('Prepared Worker: UUID must be supplied as a runtime secret; configuration endpoint removed')
