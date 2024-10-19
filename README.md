# PFDA

Learning how to create branches as my weekly tasks.

1. Make sure you're in the main branch and it is up to date with GitHub.

`git checkout main`

`git pull`

2. Create a branch from main.

`git checkout -b feature/weekly-task`

3. Once the command returns, you will be in the context of the new branch. Now you can start making changes to your files and comitting them as you normally would on main.

4. After you're done with your changes, you can go back to main and merge everything that you did on the feature/* branch to your main.

> Before proceeding, make sure you don't have any pending changes, otherwise it may fail to checkout the branch.

`git checkout main`

`git merge feature/weekly-task`

> Note that all the commits that you've made will be carried over to the main branch with this command.
