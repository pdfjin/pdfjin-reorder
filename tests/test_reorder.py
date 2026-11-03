import io, pikepdf
from pdfjin_reorder.core import reorder_pdf


def test_reorder():
    p = pikepdf.new()
    p.add_blank_page()
    p.add_blank_page()
    buf = io.BytesIO()
    p.save(buf)
    res = reorder_pdf(buf.getvalue(), [1, 0])
    with pikepdf.open(io.BytesIO(res)) as doc:
        assert len(doc.pages) == 2
