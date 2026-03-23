# Research: Simple HTML Navigation

**Branch**: `004-add-health-check` | **Date**: 2026-03-23

## Resolved Questions

### 1. Which additional page should be added?

**Decision**: Add an `/about` page.
**Rationale**: "About" is the conventional second page in a minimal web app, provides meaningful content distinct from Home, and satisfies the spec's requirement for "at least one additional route" without introducing scope creep.
**Alternatives considered**: `/contact` (no form/data needed here), `/help` (no content to fill). "About" requires no backend logic or data.

---

### 2. Flask template inheritance for consistent nav

**Decision**: Use a single `base.html` with a `<nav>` element and `{% block content %}` for page-specific content. All page templates extend `base.html`.
**Rationale**: Jinja2's `extends`/`block` is Flask's canonical pattern for shared layouts. It guarantees the nav is rendered from one source of truth on every page, satisfying FR-001 and FR-005.
**Alternatives considered**: Repeating nav HTML in each template (violates DRY, fails FR-001 consistency guarantee), server-side includes via `{% include %}` (works but `extends` is idiomatic and more structured).

---

### 3. Active page indicator without JavaScript

**Decision**: In `base.html`, compare `request.endpoint` to each route's endpoint name using a Jinja2 conditional to add an `active` CSS class and `aria-current="page"` attribute.

Example:
```html
<a href="{{ url_for('index') }}"
   class="{{ 'active' if request.endpoint == 'index' else '' }}"
   {{ 'aria-current="page"' if request.endpoint == 'index' else '' }}>Home</a>
```

**Rationale**: `request` is available in Jinja2 templates by default in Flask. This is the standard, JS-free pattern. `aria-current="page"` satisfies WCAG 2.1 SC 4.1.2 (Name, Role, Value) for screen readers.
**Alternatives considered**: Passing an `active_page` variable from each view function (more verbose, requires every route to set it; fragile if a route forgets). Template-side `request.endpoint` comparison is self-contained and declarative.

---

### 4. Semantic HTML and accessibility for the nav bar

**Decision**: Use `<nav aria-label="Main navigation">` wrapping an `<ul>` of `<li><a>` items.
**Rationale**: `<nav>` is the HTML5 landmark for navigation, enabling screen-reader landmark navigation. `aria-label` disambiguates it if multiple `<nav>` elements exist. `<ul>/<li>` structure conveys list semantics. This satisfies Constitution Principle III (WCAG 2.1 AA).
**Alternatives considered**: Plain `<div>` wrapping anchors (no landmark semantics, fails WCAG 1.3.6). `<header>` wrapping anchors directly (incorrect semantic role).

---

### 5. 404 page — nav bar must still render

**Decision**: Replace the current plain-text 404 handler with a `render_template('404.html')` response that extends `base.html`.
**Rationale**: The spec edge case states "The nav bar should still render" on unknown pages. The existing `return "Not Found", 404` plain-text response will not include the nav; a template is required.
**Alternatives considered**: Keeping plain-text 404 and adding an exception (violates spec edge case requirement).

---

### 6. CSS for active state and responsiveness

**Decision**: Include minimal inline `<style>` in `base.html` for the active link (e.g., `font-weight: bold; text-decoration: underline`) and a basic responsive rule (`flex-wrap: wrap` at narrow widths). No external CSS framework needed.
**Rationale**: The spec requires the nav to be "readable and usable at common screen widths" without requiring a full CSS library. Inline styles keep the implementation self-contained and avoid new dependencies.
**Alternatives considered**: Bootstrap or Tailwind (disproportionate for 2-page app), separate `static/style.css` (fine but adds a file for trivial rules — can be introduced in a follow-on story).
