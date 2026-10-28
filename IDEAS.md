# Ideas backlog

Format: `- [ ] **ID Title** · difficulty ★–★★★ · time · suggested stacks — spec / key edge case`
Stacks: `py` python · `js` node · `go` · `rs` rust · `web` vanilla page · `wc` web component · `react` · `dj` django
Workflow: `/pick-idea` → `/new-problem <ID> <stack>` → code → `/finish-problem`.

## A — Algorithms & data structures
- [ ] **A01 LRU cache** · ★★ · 1h · py/js/go/rs — `get`/`put` in O(1) with capacity; updating an existing key refreshes recency
- [ ] **A02 Trie + prefix search** · ★★ · 1h · py/js/go/rs — insert, `starts_with`, `autocomplete(prefix, limit)` in lexicographic order
- [ ] **A03 Interval merge** · ★ · 30m · py/js/go/rs — merge overlapping/touching intervals; unsorted input, empty input
- [ ] **A04 Binary heap / priority queue** · ★★ · 1h · py/js/go/rs — push/pop/peek with custom comparator, heapify from list
- [ ] **A05 Union-Find** · ★ · 30m · py/js/go/rs — path compression + union by rank; count components
- [ ] **A06 Dijkstra on a grid** · ★★ · 1h · py/js/go/rs — weighted cells, walls, return cost + path; unreachable target
- [ ] **A07 Topological sort** · ★★ · 1h · py/js/go/rs — Kahn's algorithm; detect and report a cycle
- [ ] **A08 Bloom filter** · ★★ · 1h · py/js/go/rs — k hash functions from two base hashes; measure false-positive rate in a test
- [ ] **A09 Consistent-hash ring** · ★★★ · 1.5h · py/go/rs — virtual nodes, add/remove node moves only ~1/n of keys
- [ ] **A10 Rate limiter** · ★★ · 1h · py/js/go/rs — token bucket and sliding window behind one interface; injectable clock
- [ ] **A11 Ring buffer** · ★ · 30m · py/js/go/rs — fixed capacity, overwrite-oldest vs reject-on-full modes
- [ ] **A12 Levenshtein distance** · ★ · 30m · py/js/go/rs — plus return the edit script
- [ ] **A13 KMP substring search** · ★★ · 1h · py/js/go/rs — build failure table, return all match offsets (overlapping too)
- [ ] **A14 Sliding-window maximum** · ★★ · 45m · py/js/go/rs — monotonic deque, O(n)
- [ ] **A15 Huffman coding** · ★★★ · 1.5h · py/js/go/rs — build tree, encode/decode round-trip, deterministic tie-breaking
- [ ] **A16 Fenwick tree** · ★★ · 45m · py/js/go/rs — point update, prefix sum, range sum
- [ ] **A17 Skip list** · ★★★ · 1.5h · py/go/rs — seedable RNG so tests are deterministic
- [ ] **A18 Sudoku solver** · ★★ · 1h · py/js/go/rs — backtracking; reject invalid boards; multiple-solution detection
- [ ] **A19 Base64 from scratch** · ★ · 30m · py/js/go/rs — encode/decode with padding, reject invalid input

## B — Scripts & CLI tools
- [ ] **B01 Nginx log summarizer** · ★★ · 1h · py/js/go/rs — top paths, status histogram, p95 latency from combined log format; skip malformed lines
- [ ] **B02 Duplicate-file finder** · ★★ · 1h · py/js/go/rs — group by size, then by hash; never follow symlink loops
- [ ] **B03 Markdown TOC generator** · ★ · 45m · py/js/go/rs — GitHub-style anchors, duplicate headings get `-1`, ignore fenced code
- [ ] **B04 CSV → JSON with type inference** · ★★ · 1h · py/js/go/rs — ints/floats/bools/null; quoted fields with commas and newlines
- [ ] **B05 Bulk rename** · ★★ · 1h · py/js/go/rs — regex find/replace, `--dry-run`, refuse collisions
- [ ] **B06 .env diff/lint** · ★ · 45m · py/js/go/rs — missing/extra keys, duplicates, unquoted spaces
- [ ] **B07 Git-log stats** · ★★ · 1h · py/js/go/rs — commits per author/week from `git log --numstat` text
- [ ] **B08 Cron next-N runs** · ★★★ · 2h · py/js/go/rs — `*/5`, ranges, lists, day-of-month OR day-of-week rule
- [ ] **B09 du-style tree** · ★★ · 1h · py/js/go/rs — human-readable sizes, depth limit, sort by size
- [ ] **B10 JSON diff** · ★★ · 1h · py/js/go/rs — path-based added/removed/changed output; array handling documented
- [ ] **B11 TODO/FIXME scanner** · ★ · 45m · py/js/go/rs — file:line report, ignore globs, respect `.gitignore`-lite
- [ ] **B12 Conventional-commits changelog** · ★★ · 1h · py/js/go/rs — group feat/fix/BREAKING, link-free markdown output
- [ ] **B13 Word-frequency counter** · ★ · 30m · py/js/go/rs — unicode words, stop-word list, stable tie-break

## C — Web / JS widgets
- [ ] **C01 Debounce / throttle** · ★ · 30m · js/web — leading/trailing options, `cancel`, fake timers
- [ ] **C02 Autocomplete** · ★★ · 1.5h · web/react — keyboard nav, abort stale requests, highlight matches
- [ ] **C03 Drag-to-sort list** · ★★ · 1.5h · web — pointer events, keyboard alternative, emits new order
- [ ] **C04 Tiny redux-like store** · ★★ · 1h · js/web — `dispatch`, `subscribe`, `combineReducers`, middleware
- [ ] **C05 Modal with focus trap** · ★★ · 1h · web/wc — Tab cycling, Esc closes, restores focus
- [ ] **C06 Infinite scroll** · ★★ · 1h · web/react — IntersectionObserver (mocked), page loading states, end-of-list
- [ ] **C07 Toast manager** · ★★ · 1h · web/react — queue, max visible, auto-dismiss, pause on hover
- [ ] **C08 Accessible tabs** · ★★ · 1h · web/wc — ARIA roles, arrow-key roving tabindex, Home/End
- [ ] **C09 Virtualized list** · ★★★ · 2h · web/react — render only visible window; compute range from scrollTop
- [ ] **C10 Color-contrast checker** · ★ · 45m · js/web — WCAG ratio, AA/AAA pass/fail, 3/6-digit hex
- [ ] **C11 Sortable/filterable table** · ★★ · 1.5h · web/react — multi-column sort, text filter, stable sort
- [ ] **C12 `<tag-input>`** · ★★ · 1.5h · wc — add on Enter/comma, remove with Backspace, `change` event, form-associated value
- [ ] **C13 `<star-rating>`** · ★ · 1h · wc — attributes ↔ properties, keyboard, half stars
- [ ] **C14 React `useDebounce` / `useLocalStorage`** · ★★ · 1h · react — SSR-safe, cross-tab `storage` event
- [ ] **C15 React todo with reducer** · ★ · 1h · react — add/toggle/delete/filter, persisted order
- [ ] **C16 Django notes CRUD + auth** · ★★ · 2h · dj — per-user ownership; other users get 404
- [ ] **C17 Django short links** · ★★ · 1.5h · dj — slug generation, click counter, expiry
- [ ] **C18 Django paginated JSON endpoint** · ★★ · 1h · dj — `?page`/`?page_size`, stable ordering, invalid params → 400

## D — Systems / interview-style
- [ ] **D01 Calculator (tokenizer + parser)** · ★★ · 1.5h · py/js/go/rs — precedence, parens, unary minus, `^` right-assoc, error positions
- [ ] **D02 JSON parser** · ★★★ · 2h · py/js/go/rs — no stdlib parser; escapes, unicode, error messages with line/col
- [ ] **D03 Mini regex engine** · ★★★ · 2h · py/js/go/rs — `. * + ? | ()` and anchors via NFA or backtracking
- [ ] **D04 Mini template engine** · ★★ · 1.5h · py/js/go/rs — `{{ var }}`, `{% for %}`, `{% if %}`, HTML escaping
- [ ] **D05 Event emitter** · ★ · 30m · js/py/go/rs — `on/once/off/emit`, listener order, errors in a listener
- [ ] **D06 Promise from scratch** · ★★★ · 2h · js — A+ semantics: chaining, thenable adoption, async ordering
- [ ] **D07 KV store with TTL** · ★★ · 1h · py/js/go/rs — lazy + active expiry, injectable clock, `incr`
- [ ] **D08 Dependency task scheduler** · ★★ · 1.5h · py/js/go/rs — run DAG with N workers, fail-fast, order guarantees
- [ ] **D09 Stack VM interpreter** · ★★ · 1.5h · py/js/go/rs — push/add/jmp/call/ret; stack-underflow errors
- [ ] **D10 LCS diff** · ★★ · 1h · py/js/go/rs — line diff with unified-style output
- [ ] **D11 Semver comparator** · ★★ · 1h · py/js/go/rs — prerelease ordering rules, ranges `^ ~ >=`
- [ ] **D12 Glob matcher** · ★★ · 1h · py/js/go/rs — `* ? [a-z] **`, path-separator rules
- [ ] **D13 URL router with params** · ★★ · 1h · py/js/go/rs — `/users/:id`, wildcard, precedence of static over dynamic
- [ ] **D14 INI / TOML-lite parser** · ★★ · 1.5h · py/js/go/rs — sections, typed values, inline comments, error lines
- [ ] **D15 JSONPath-lite** · ★★ · 1.5h · py/js/go/rs — `$.a.b[0]`, `[*]`, `..key`, filters `[?(@.x>1)]`

## E — Protocols & mini servers
- [ ] **E01 IP/UDP/TCP header parser** · ★★ · 1.5h · py/go/rs — parse Ethernet→IPv4→TCP/UDP from hex dump fixtures; verify IPv4 checksum
- [ ] **E02 DNS message parser + builder** · ★★★ · 2h · py/go/rs — name compression pointers, A/AAAA/CNAME/TXT, round-trip
- [ ] **E03 DNS stub UDP server** · ★★★ · 2h · py/go/rs — answers from an in-memory zone, NXDOMAIN, truncation bit
- [ ] **E04 TLV decoder** · ★ · 45m · py/go/rs — nested TLVs, multi-byte lengths (BER style), truncated input
- [ ] **E05 Protobuf wire decoder** · ★★ · 1.5h · py/go/rs — varints, zigzag, length-delimited, unknown fields
- [ ] **E06 MQTT packet parser** · ★★ · 1.5h · py/go/rs — CONNECT/PUBLISH/SUBSCRIBE, remaining-length varint, QoS flags
- [ ] **E07 WebSocket frame parser** · ★★ · 1h · py/go/rs — masking, extended lengths, fragmentation, control frames
- [ ] **E08 HTTP/1.1 request parser** · ★★ · 1.5h · py/go/rs — from raw bytes, chunked bodies, header folding rejected, partial reads
- [ ] **E09 Redis RESP parser** · ★★ · 1h · py/go/rs — all five types, nested arrays, incremental feed
- [ ] **E10 PNG chunk reader** · ★★ · 1h · py/go/rs — signature, chunk CRC32, extract IHDR + text chunks
- [ ] **E11 pcap file reader** · ★★ · 1.5h · py/go/rs — both endiannesses, iterate packets, feed into E01
- [ ] **E12 STUN binding request** · ★★ · 1.5h · py/go/rs — build request, parse XOR-MAPPED-ADDRESS; local fake server in tests
- [ ] **E13 SOCKS5 handshake** · ★★ · 1.5h · py/go/rs — no-auth method negotiation + CONNECT; local echo target in tests
- [ ] **E14 Length-prefixed TCP framing** · ★★ · 1h · py/go/rs — frames split across reads, coalesced frames, max size
- [ ] **E15 UDP echo / chat server** · ★ · 1h · py/go/rs — join/leave/broadcast over UDP, ephemeral ports
- [ ] **E16 UDP stop-and-wait ARQ** · ★★★ · 2h · py/go/rs — seq numbers, ACK, retransmit on drop; lossy-socket wrapper in tests
- [ ] **E17 TLS echo server** · ★★ · 1.5h · py/go/rs — self-signed cert from `shared/certs`, client verifies against it
- [ ] **E18 TLS client + cert inspector** · ★★ · 1.5h · py/go/rs — handshake with local TLS test server, print subject/SAN/expiry, GET `/`
