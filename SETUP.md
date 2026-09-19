# Setup

This version follows the reference repository's structure: a short README and separate animated SVG assets, data, scripts and a GitHub Actions workflow. The reference repository itself has these separate assets and a 43-line README.

1. Upload every file in this package to the root of `PERO-99/PERO-99`.
2. In **Settings → Actions → General**, allow **Read and write permissions** for workflows if necessary.
3. Open **Actions → Update profile art → Run workflow**.
4. Refresh the profile page.

The workflow queries the repository owner's contribution calendar through GitHub GraphQL using the automatically provided Actions token and regenerates the heatmap. The top portrait and wordmark are animated SVGs.
