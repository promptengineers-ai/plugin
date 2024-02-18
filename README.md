<h1 align="center">
  🤖 Prompt Engineers AI - Plugin API 
</h1>
<p align="center">
Sample Agent Plugin Application for promptengineers.ai agents.
</p>
<p align="center">
  <a href="https://prompt-engineers.gitbook.io/documentation/plugin"><img src="https://img.shields.io/badge/View%20Documentation-Docs-yellow"></a>
  <a href="https://promptengineersai.slack.com/ssb/redirect"><img src="https://img.shields.io/badge/Join%20our%20community-Slack-blue"></a>
  <!-- <a href="https://pepy.tech/project/prompttools" target="_blank"><img src="https://static.pepy.tech/badge/prompttools" alt="Total Downloads"/></a> -->
  <!-- <a href="https://github.com/promptengineers-ai/llm-server">
      <img src="https://img.shields.io/github/stars/promptengineers-ai/llm-server" />
  </a> -->
  <!-- <a href="https://www.youtube.com/@promptengineersai"><img src="https://img.shields.io/youtube/channel/views/UCpGq31VRTZ9JzosUFA_HWzw?label=@promptengineersai
"></a> -->
</p>
<!-- <p align="center">
  <video autoplay loop muted playsinline>
    <source src="https://github.com/promptengineers-ai/llm-server/blob/development/static/demos/chat-ui-demo.mp4?raw=true" type="video/mp4">
    Your browser does not support the video tag.
  </video>
</p> -->

<!-- <p align="center">
  <img src="https://github.com/promptengineers-ai/llm-server/blob/development/static/demos/llm-server.gif?raw=true" />
</p> -->

### Useful Links
- [Deploying FastAPI to Vercel](https://blog.logrocket.com/deploying-fastapi-applications-to-vercel/)


## 🛠️ Server Setup and Usage
```bash
### Setup Virtual Env
python3 -m venv .venv

### Activate Virtual Env
source .venv/bin/activate

### Install Runtime & Dev Dependencies
pip install -r requirements.txt

### Install Runtime Dependencies
pip install -r requirements.txt

### Run Application on local machine
bash scripts/dev.sh
```

### Environment Variables
<table border="1" width="100%">
  <tr>
    <th>Variable Name</th>
    <th>Example</th>
    <th>Description</th>
  </tr>
  <tr>
    <td>VERCEL_ENV</td>
    <td>production</td>
    <td>production|preview|development</td>
  </tr>
  <tr>
    <td>VERCEL_URL</td>
    <td>plugin.promptengineers.ai</td>
    <td>Domain for the API server</td>
  </tr>
</table>

## Deploy
1. Log in to vercel
```bash
vercel login
```

2. Deploy to vercel
```bash
vercel . --prod
```

## 🤝 How to Contribute

We welcome contributions from the community, from beginners to seasoned developers. Here's how you can contribute:

1. **Fork the repository**: Click on the 'Fork' button at the top right corner of the repository page on GitHub.

2. **Clone the forked repository** to your local machine: `git clone <forked_repo_link>`.

3. **Navigate to the project folder**: `cd llm-server`.

4. **Create a new branch** for your changes: `git checkout -b <branch_name>`.

5. **Make your changes** in the new branch.

6. **Commit your changes**: `git commit -am 'Add some feature'`.

7. **Push to the branch**: `git push origin <branch_name>`.

8. **Open a Pull Request**: Go back to your forked repository on GitHub and click on 'Compare & pull request' to create a new pull request.

Please ensure that your code passes all the tests and if possible, add tests for new features. Always write a clear and concise commit message and pull request description.

## 💡 Issues

Feel free to submit issues and enhancement requests. We're always looking for feedback and suggestions.

## 🤓 Maintainers

- `Ryan Eggleston` - `ryan.adaptivebiz@gmail.com`

## 📜 License

This project is open-source, under the [MIT License](LICENSE). Feel free to use, modify, and distribute the code as you please.

Happy Prompting! 🎉🎉