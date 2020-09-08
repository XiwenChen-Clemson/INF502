# Git/GitHub Assignment



## Part 1: Dealing with git

To conduct this, you will have to download [handson.zip](handson.zip) and unzip it.
handson folder is a git repository. Using the command line change the directory to "handson/"


```
cd./handson
```

### 1. Describe what is the output of the following commands
#### Description
    -  `git branch` ：List the existed branches on the repo
    -  `git checkout BRANCH_NAME` ：switch to specified branch
    -  `git log --decorate`：demonstrate related information (such as HEAD, branches name, tag names, etc)
    that point to each commit. For this repo, 
#### Codes and ouputs
```
>git branch
* master
  math
>git checkout math
Switched to branch 'math'
>git log --decorate
commit 18931d12a8be7cac049b73c6bc8136e9482f3371 (HEAD -> master)
Author: Igor Steinmacher <igorsteinmacher@gmail.com>
Date:   Wed Aug 14 23:15:28 2019 -0700

    Making a small change here

commit 654b490a181dedf82dd6deda5f9848d6cca05918
Author: Igor Steinmacher <igorsteinmacher@gmail.com>
Date:   Wed Aug 14 23:12:14 2019 -0700

    Added a draft of A.py

commit 2dfb02c3f9383d6c3b2695c99e175d8b85f594a1
Author: Igor Steinmacher <igorsteinmacher@gmail.com>
Date:   Wed Aug 14 23:08:47 2019 -0700

     Creating all files (all empty)

C:\Users\tthet\Desktop\handson\handson>git checkout math
Switched to branch 'math'

C:\Users\tthet\Desktop\handson\handson>git log --decorate
commit e3c629dd524712aedea96d7dbaad1c50d12b5b5e (HEAD -> math)
Author: Igor Steinmacher <igorsteinmacher@gmail.com>
Date:   Wed Aug 14 23:13:48 2019 -0700

    Adding some more knowledge to the function

commit 654b490a181dedf82dd6deda5f9848d6cca05918
Author: Igor Steinmacher <igorsteinmacher@gmail.com>
Date:   Wed Aug 14 23:12:14 2019 -0700

    Added a draft of A.py

commit 2dfb02c3f9383d6c3b2695c99e175d8b85f594a1
Author: Igor Steinmacher <igorsteinmacher@gmail.com>
Date:   Wed Aug 14 23:08:47 2019 -0700

     Creating all files (all empty)


```

### 2. Try `git log --graph --all`. What do you see?
#### Description
`git log --graph --all` can draw an ASCII graph representing the branch structure of the commit history.
#### Codes and ouputs
```
>git log --graph --all
* commit 18931d12a8be7cac049b73c6bc8136e9482f3371 (master)
| Author: Igor Steinmacher <igorsteinmacher@gmail.com>
| Date:   Wed Aug 14 23:15:28 2019 -0700
|
|     Making a small change here
|
| * commit e3c629dd524712aedea96d7dbaad1c50d12b5b5e (HEAD -> math)
|/  Author: Igor Steinmacher <igorsteinmacher@gmail.com>
|   Date:   Wed Aug 14 23:13:48 2019 -0700
|
|       Adding some more knowledge to the function
|
* commit 654b490a181dedf82dd6deda5f9848d6cca05918
| Author: Igor Steinmacher <igorsteinmacher@gmail.com>
| Date:   Wed Aug 14 23:12:14 2019 -0700
|
|     Added a draft of A.py
|
* commit 2dfb02c3f9383d6c3b2695c99e175d8b85f594a1
  Author: Igor Steinmacher <igorsteinmacher@gmail.com>
  Date:   Wed Aug 14 23:08:47 2019 -0700

       Creating all files (all empty)
```

### 3. Use `git diff BRANCH_NAME` to view the differences from a branch and the current branch.
   Summarize the difference from master to the other branch.

```
The rusults show the diffence between two branches by using + and -.
In which, + means the content of the file only in current branch, whihe - means the content in the compared branch.
The difference shows that in A.py, master branch has two other opreators (sum, subtraction) with printable results,
and  nothing different in B.py

```

### 4. Write a command sequence to merge the non-master branch into `master`

```
>git checkout master
>git merge math
```


### 5. Write a command (or sequence) to (i) create a new branch called `math` (from the `master`) 
and (ii) change to this branch (yes, `math` is already there, just report what you've done, the error and the reason you got the error. If you deleted and recreated the branch, you are fine too)

```
>git branch math
>git checkout math

```
   
### 6. Edit B.py adding the following source code below the content you have there
```
print 'I know math, look:'
print 2+2
```

### 7. Write a command (or sequence) to commit your changes
```
>git add B.py
>git commit -m "added two lines in B.py"

```

### 8. Change back to the `master` branch and change B.py adding the following source code (commit your change to `master`):
```
print 'hello world!'

```
```
>git checkout master
>git add B.py
>git commit -m "added one line in B.py"
```

### 9. Write a command sequence to merge the `math` branch into `master` and describe what happened
```
>git merge math
Auto-merging B.py
CONFLICT (content): Merge conflict in B.py
Automatic merge failed; fix conflicts and then commit the result.
```
   
### 10. Write a set of commands to abort the merge
```
>git merge --abort

```
   
### 11. Now repeat item 9, but proceed with the manual merge (Editing B.py). All implemented functions are needed. Explain your procedure
```
step 1:Abort the merge:
>git merge --abort
>git reset --merge
step 2:Edit B.py by deleting the two lines/the one line. Only modify one of them. manually.
step 3:commit the modification
>git add B.py
>git commit -m "maunual modified B"
step 4: merge again
>git merge math
```

### 12. Write a command (or set of commands) to proceed with the merge and make `master` branch up-to-date
```
## This part implemented on Git Bash
$ git merge --abort
$ git reset --merge
$ vim B.py
$ git commit -m "modified B"
$ git merge math


```
