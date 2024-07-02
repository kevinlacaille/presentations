It looks like `pyenv-virtualenv` might not be properly configured in your shell. Let's ensure it's correctly set up.

### Full Setup and Activation Command Sequence

1. **Install pyenv and pyenv-virtualenv**:
   ```sh
   brew install pyenv
   brew install pyenv-virtualenv
   ```

2. **Install the desired Python version using pyenv**:
   ```sh
   pyenv install 3.11.4
   ```

3. **Create a new virtual environment using pyenv-virtualenv**:
   ```sh
   pyenv virtualenv 3.11.4 scipy2024-env
   ```

4. **Configure your shell to use pyenv and pyenv-virtualenv**:
   Add the following to your `~/.zshrc` or `~/.bashrc`:

   ```sh
   export PYENV_ROOT="$HOME/.pyenv"
   export PATH="$PYENV_ROOT/bin:$PATH"
   eval "$(pyenv init --path)"
   eval "$(pyenv init -)"
   eval "$(pyenv virtualenv-init -)"
   ```

5. **Reload your shell configuration**:
   ```sh
   source ~/.zshrc  # or source ~/.bashrc
   ```

6. **Activate the virtual environment**:
   ```sh
   pyenv activate scipy2024-env
   ```

### Install OpenCV

Once the environment is activated, install OpenCV:

```sh
pip install --upgrade pip
pip install -r requirements.txt
```
