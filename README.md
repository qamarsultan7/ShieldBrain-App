# ShieldBrain Website

Static marketing site for ShieldBrain, published from the `website/` directory.

## GitHub Pages deployment

The workflow in `.github/workflows/deploy-pages.yml` deploys every push to `main`.

1. Push this repository to GitHub.
2. In **Settings > Pages**, set **Source** to **GitHub Actions**.
3. The custom domain is `shieldbrain-app.lunarforge.dev`. Its DNS must point to GitHub Pages, and `website/CNAME` must contain that exact domain.

The production site is available at https://shieldbrain-app.lunarforge.dev/.
