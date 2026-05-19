"""
Core routes blueprint.
Handles main application routes like landing page.
"""

from flask import Blueprint, render_template, session, redirect, url_for
from datetime import datetime


core_bp = Blueprint('core', __name__)


@core_bp.route('/')
def landing():
    """Landing page route.

    V1 is archived. The site now shows a restructuring notice while V2 is
    built separately. The original landing page is preserved untouched at
    templates/landing.html and can be restored by rendering it here again.
    """
    timestamp = datetime.utcnow().strftime('%Y%m%d%H%M%S')
    return render_template('restructuring.html', timestamp=timestamp)
