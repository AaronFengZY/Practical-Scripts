Written By ZhiYuan Feng


Below is a **step-by-step** outline of how to **pull changes** from an **upstream repository** into **your fork**—and then push those changes to **your own GitHub** fork. This includes handling merge conflicts, **without** using a rebase workflow.

---

# Complete Workflow for Merging Upstream Into Your Fork

## 1. Ensure You Have an Upstream Remote

1. In your local repository, check which remotes are defined:
   ```bash
   git remote -v
   ```
2. You should see something like:
   ```text
   origin   https://github.com/<YOUR_USERNAME>/<YOUR_FORK>.git (fetch)
   origin   https://github.com/<YOUR_USERNAME>/<YOUR_FORK>.git (push)
   upstream https://github.com/<ORIGINAL_OWNER>/<ORIGINAL_REPO>.git (fetch)
   upstream https://github.com/<ORIGINAL_OWNER>/<ORIGINAL_REPO>.git (push)
   ```
3. If you **don’t** see `upstream`, add it:
   ```bash
   git remote add upstream https://github.com/<ORIGINAL_OWNER>/<ORIGINAL_REPO>.git
   ```

---

## 2. Fetch Changes from Upstream

1. Update your local copy of all remote branches (including `upstream`):
   ```bash
   git fetch upstream
   ```
2. Confirm which branches exist on `upstream`:
   ```bash
   git branch -r
   ```
   You should see something like `upstream/master`, `upstream/demo`, etc.

---

## 3. Check Out the Local Branch You Want to Update

1. For instance, if you want to pull changes into your local **`hoimoge`** branch:
   ```bash
   git checkout hoimoge
   ```
2. Verify you’re on that branch:
   ```bash
   git branch
   ```
   You should see:
   ```
   * hoimoge
     master
   ```

---

## 4. Merge from Upstream Master

To bring in changes from `upstream/master`:

```bash
git merge upstream/master
```

- Git will create a **merge commit** that combines upstream’s changes and your local commits.
- If there are conflicts, Git will stop and list which files need your attention.

---

## 5. Resolve Merge Conflicts (If Any)

If you see messages like:
```
Automatic merge failed; fix conflicts and then commit the result.
```
or
```
CONFLICT (content): Merge conflict in <filename>
```

1. **Open the conflicting files** in your editor.  
2. Look for conflict markers:
   ```diff
   <<<<<<< HEAD
   (Your local changes)
   =======
   (Upstream changes)
   >>>>>>> upstream/master
   ```
3. **Decide** which lines to keep—maybe some combination of both.
4. **Remove** the conflict markers (`<<<<<<<`, `=======`, `>>>>>>>`).
5. **Save** the file.
6. **Mark** the file as resolved:
   ```bash
   git add <the_conflicted_file>
   ```
7. **Commit** to finalize the merge:
   ```bash
   git commit
   ```
   (Git might auto-generate a merge commit message; feel free to edit it.)

---

## 6. Verify the Merge

1. **Check your commit history**:
   ```bash
   git log --oneline --graph --decorate
   ```
   You should see a **merge commit** that says something like “Merge branch ‘master’ of github.com/ORIGINAL_OWNER/ORIGINAL_REPO…”.

2. **Check your status**:
   ```bash
   git status
   ```
   Ensure it doesn’t list any unmerged paths.

---

## 7. Push Changes to Your Fork

Finally, push your merged branch to **your fork** (the `origin` remote):

```bash
git push origin hoimoge
```

No force-push is necessary, because merging doesn’t rewrite history.

---

## 8. Confirm on GitHub

1. Go to **GitHub** in your browser.  
2. Navigate to **your fork**’s repository.  
3. Switch to the **hoimoge** branch.  
4. You should see the **merge commit** in your commit history.

---

# Summary

1. **Add/Confirm** the “upstream” remote.  
2. **Fetch** the latest upstream changes: `git fetch upstream`.  
3. **Check out** your local branch (e.g. `hoimoge`).  
4. **Merge** from the `upstream/master` branch: `git merge upstream/master`.  
5. **Resolve conflicts** (if any) and **commit**.  
6. **Push** your now-updated `hoimoge` branch back to your fork: `git push origin hoimoge`.  
7. **Check** GitHub to confirm everything looks correct.