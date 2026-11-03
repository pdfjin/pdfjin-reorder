import io
from pathlib import Path
from typing import List, Union
import pikepdf


def reorder_pdf(input_pdf: Union[str, Path, bytes], order: List[int], output: Union[str, Path] = None) -> bytes:
    src = pikepdf.open(str(input_pdf)) if isinstance(input_pdf, (str, Path)) else pikepdf.open(io.BytesIO(input_pdf))
    new_pdf = pikepdf.new()

    with src:
        for idx in order:
            if 0 <= idx < len(src.pages):
                new_pdf.pages.append(src.pages[idx])

        buf = io.BytesIO()
        new_pdf.save(buf)
        res = buf.getvalue()

    if output:
        Path(output).write_bytes(res)
    return res
