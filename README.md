/**************Basic Setup**************/
1. mkdir ml-project             //To create a directory named "ml-project"
2. cd ml-project                //To navigate to the directory
3. git init                     //To initialize Git repository
4. touch <filenames>            //To create files
5. git status                   //To check status of the git repository

/**************Version Control Workflow**************/
1. git add <filename>                           //To stage files
2. git commit -m "commit-message" <filename>    //To commit files. "-m" -> commit message
3. To create a repository in GitHub
    -> Open GitHub
    -> Select Repository
    -> Click "New"
    -> Enter Repository Name
    -> Click "Create Repository"
4. To link local repository to the GitHub repository and push
    -> Copy the GitHub repository link
    -> In git type the following commands
        - git remote add origin <GitHub_Repository_Link> //To add local repository to the GitHub repository
        - git push -u origin master                      //To push your local changes to GitHub. "-u" is to upstream for the branch. "master" specifies the
                                                           local branch to be pushed to GitHub.

/**************Mini-Project - Collaborative Workflow**************/
1. In GitHub create files "predict.py" and update "README.md" and commit it.
2. Update "utils.py" and create "config.py"
3. Use "git pull" to retrive changes from GitHub
4. Since there is already a README.md file which is not staged for commit in local repository, there will be merge conflict.
5. The conflict has to be resolved manually by merging the branches by stashing or deleting the empty read me file and needs to be committed.

/**************Best Practices for Collaborative Workflow**************/
1. Create feature branches from the main branch
2. For controlled releases with large team, it's better to use production (main) and integration branch, than directly pushing into main branch.
3. Clear commit messages
4. Pull request - pull latest changes, review the code logic not only syntax, discuss with teammates before merging. description of what is added and why.
5. For local repositories - authors should pull latest changes frequently before the start editing the file to avoid merge conflicts.
6. Commit error free codes as soon as possible to avoid resolving large conflicts.
7. Communicate with teammates before fixing merge conflicts, never delete code blindly.
8. Avoid hardcoding passwords and API keys. Instead use ".gitignore" and ".env" to store API keys and confidential files.