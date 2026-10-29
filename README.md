# Case handoff workbench

Build a browser workspace for Northstar Services, a fictional operations team.

## Start the page

Choose **Use this template**, create your repository and clone it. From that repository's root,
with Node.js 24 and pnpm 12.3.4 installed:

```sh
pnpm install --frozen-lockfile
pnpm dev
```

Open the local address printed in the terminal. You should see **Case handoff workbench** and
**Your React starter is running.** Edit src/App.jsx and save to see your change in the browser.
Stop the server with Ctrl+C. Run `pnpm build` to build the frontend; `pnpm preview` serves that
build locally. A frontend build is not a deployed or completed client application.

Installation help: [Node.js](https://nodejs.org/en/download) and
[pnpm](https://pnpm.io/installation). This starter uses [React](https://react.dev/learn) and
[Vite](https://vite.dev/guide/).

## Build the client's workspace

1. Read CLIENT_BRIEF.md for the five requested features and the handover journey.
2. Read LEARNER_GUIDE.md for the input contract, course work and submission requirements.
3. A useful first milestone is to create a batch, save one fictional note and open it again.
   This is a suggested starting point; choose the implementation and verification yourself.
4. Extend that working slice to the remaining client features. Create your FastAPI backend with
   uv and connect it to the page. The backend, storage and model integration are yours to design.

The supplied page is only a running starting point. The frontend setup and its existing build
command are provided work, not evidence that you implemented the client features or engineering
checks. No backend, model integration, test suite or evaluation dataset is included.
Use fictional information only. The trainer provides approved service access and the current
data/tool policy separately; you can start the non-model work while that access is arranged.

Continue your completed project and saved information in Week 2. There is no second starter.
Disclose any reused code or material, including material from earlier versions of this repository.
