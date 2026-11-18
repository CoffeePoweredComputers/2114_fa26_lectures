#!/usr/bin/env python3
"""Serve the current dir; POST /result?engine=<name> saves the body to
result-<engine>.json next to it.  Usage: serve3.py <port>"""
import http.server
import socketserver
import sys
from urllib.parse import urlparse, parse_qs


class Handler(http.server.SimpleHTTPRequestHandler):
    def do_POST(self):
        parsed = urlparse(self.path)
        if parsed.path != '/result':
            self.send_response(404)
            self.end_headers()
            return
        engine = (parse_qs(parsed.query).get('engine') or ['unknown'])[0]
        safe = ''.join(c if c.isalnum() or c in '-_' else '_' for c in engine)
        length = int(self.headers.get('Content-Length', 0) or 0)
        body = self.rfile.read(length) if length else b''
        with open('result-%s.json' % safe, 'wb') as fh:
            fh.write(body)
        self.send_response(204)
        self.send_header('Access-Control-Allow-Origin', '*')
        self.end_headers()

    def log_message(self, fmt, *args):
        pass


class ThreadingServer(socketserver.ThreadingMixIn, http.server.HTTPServer):
    daemon_threads = True
    allow_reuse_address = True


if __name__ == '__main__':
    port = int(sys.argv[1]) if len(sys.argv) > 1 else 8765
    with ThreadingServer(('127.0.0.1', port), Handler) as httpd:
        httpd.serve_forever()
