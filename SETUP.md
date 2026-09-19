# Setup

This version uses **GIF frames instead of CSS-animated SVGs** because GitHub README image rendering can freeze or ignore CSS/SVG animation.

The reference repository is also asset-driven: its repository contains a short README plus separate portrait, contribution, wordmark, source-image, script, data and workflow files.

1. Upload all files to `PERO-99/PERO-99`.
2. Keep the repository public.
3. In **Settings → Actions → General**, allow workflows to have **Read and write permissions**.
4. Run **Actions → Update contribution animation → Run workflow**.
5. Refresh the profile.

The top animations are self-contained GIFs and should loop continuously in GitHub's README renderer.


## Contribution Snake

The repository now also uses the official `Platane/snk` GitHub Action to turn the
real GitHub contribution calendar into an animated snake. The action supports GIF
and SVG outputs and can run daily. The workflow publishes the generated GIF to
the `output` branch, and the README embeds that generated file.

After uploading the files:

1. Open **Settings → Actions → General**.
2. Under **Workflow permissions**, select **Read and write permissions**.
3. Open **Actions → Generate contribution snake**.
4. Click **Run workflow**.
5. Wait for the workflow to finish.
6. Refresh your profile.

The first run creates the `output` branch and the `github-contribution-grid-snake.gif`
asset. The README will then display the animation under the contribution section.
