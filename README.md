# ShieldBrain Website

Static marketing site for ShieldBrain, published from the `website/` directory.

## GitHub Pages deployment

The workflow in `.github/workflows/deploy-pages.yml` deploys every push to `main`.

1. Push this repository to GitHub.
2. In **Settings → Pages**, set **Source** to **GitHub Actions**.
3. To use `shieldbrain.app`, point its DNS records to GitHub Pages as described in GitHub's custom-domain documentation. The committed `website/CNAME` file configures the deployed site domain.

For a repository URL, the site is available at `https://<owner>.github.io/<repository>/`. For the custom domain, it is available at `https://shieldbrain.app/` after DNS and certificate provisioning complete.
