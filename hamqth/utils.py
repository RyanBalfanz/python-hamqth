from collections import defaultdict

def etree_to_dict(t):
    """https://stackoverflow.com/a/10076823"""
    d = {t.tag: {} if t.attrib else None}
    children = list(t)
    if children:
        dd = defaultdict(list)
        for dc in map(etree_to_dict, children):
            for k, v in dc.items():
                dd[k].append(v)
        d = {t.tag: {k: v[0] if len(v) == 1 else v for k, v in dd.items()}}
    if t.attrib:
        d[t.tag].update(('@' + k, v) for k, v in t.attrib.items())
    if t.text:
        text = t.text.strip()
        if children or t.attrib:
            if text:
                d[t.tag]['#text'] = text
        else:
            d[t.tag] = text
    return d

# def get_session_id(username, password):
#     ns = HAMQTH_NAMESPACE
#     url = HAMQTH_URL
#     payload = dict(u=username, p=password)
#     response = requests.get(url, params=urlencode(payload))
#     if not response.ok:
#         response.raise_for_status()
#     root = ET.fromstring(response.text)
#     session = root.find("hamqth:session", ns)
#     session_id = session.find("hamqth:session_id", ns)
#     if session_id is None:
#         error = session.find("hamqth:error", ns)
#         raise Exception(error.text)
#     return session_id.text

# def search_callsign(session_id, query, program_name):
#     ns = HAMQTH_NAMESPACE
#     url = HAMQTH_URL
#     payload = dict(id=session_id, callsign=query, prg=program_name)
#     response = requests.get(url, params=urlencode(payload))
#     if not response.ok:
#         response.raise_for_status()
#     root = ET.fromstring(response.text)
#     search = root.find("hamqth:search", ns)
#     if search is None:
#         session = root.find("hamqth:session", ns)
#         error = session.find("hamqth:error", ns)
#         raise Exception(error.text)
#     return search
