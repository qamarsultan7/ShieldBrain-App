# ShieldBrain Website

Static marketing site for ShieldBrain, published from the `website/` directory.

## GitHub Pages deployment

The workflow in `.github/workflows/deploy-pages.yml` deploys every push to `main`.

1. Push this repository to GitHub.
2. In **Settings â†’ Pages**, set **Source** to **GitHub Actions**.
3. To use `shieldbrain.app`, first register the domain and then point its DNS records to GitHub Pages as described in GitHub's custom-domain documentation. Add a `website/CNAME` file containing `shieldbrain.app` when the domain is ready.

For a repository URL, the site is available at `https://qamarsultan7.github.io/ShieldBrain-App/`. For the custom domain, it is available at `https://shieldbrain.app/` after DNS and certificate provisioning complete.
