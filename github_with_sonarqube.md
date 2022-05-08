# github_with_sonarqube

![Img](./FILES/github_with_sonarqube.md/b994ee08.png)


test github repo
```
https://github.com/yhkl-dev/test_sonarcloud_repo
```

grant sonarcloud permission

![Img](./FILES/github_with_sonarqube.md/c240f9fb.png)

click config
![Img](./FILES/github_with_sonarqube.md/2334c47b.png)

click select repositories to choose which repo you want analyze with sonarcloud
![Img](./FILES/github_with_sonarqube.md/97996c08.png)

back to sonarcloud
![Img](./FILES/github_with_sonarqube.md/88312297.png)

click set up button
![Img](./FILES/github_with_sonarqube.md/ba298579.png)

choose github actions

![Img](./FILES/github_with_sonarqube.md/1dce62e0.png)

configure your github settings of your repo


![Img](./FILES/github_with_sonarqube.md/a2a6e23b.png)

![Img](./FILES/github_with_sonarqube.md/7e72499b.png)

click add secret

back to sonarcloud

![Img](./FILES/github_with_sonarqube.md/190a38ff.png)

choose your proejct language: 

![Img](./FILES/github_with_sonarqube.md/d06e1a1a.png)

copy the content and create 
`.github/workflows/build.yml` file in your repo

```
name: Build
on:
  push:
    branches:
      - master
  pull_request:
    types: [opened, synchronize, reopened]
jobs:
  sonarcloud:
    name: SonarCloud
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v2
        with:
          fetch-depth: 0  # Shallow clones should be disabled for a better relevancy of analysis
      - name: SonarCloud Scan
        uses: SonarSource/sonarcloud-github-action@master
        env:
          GITHUB_TOKEN: ${{ secrets.GITHUB_TOKEN }}  # Needed to get PR information, if any
          SONAR_TOKEN: ${{ secrets.SONAR_TOKEN }}
```


![Img](./FILES/github_with_sonarqube.md/02e1b3f3.png)

paste the content such as follows

![Img](./FILES/github_with_sonarqube.md/c41567bf.png)

commit your change 

> sonarcloud with analyze your code on master branch and when open/synchronize/reopen a new pull request

back to sonarcloud
![Img](./FILES/github_with_sonarqube.md/89dd9e21.png)

click continue

![Img](./FILES/github_with_sonarqube.md/79fa7ed8.png)

create config file in your root directory of the proejct
and name `it sonar-project.properties`

```
sonar.projectKey=yhkl-dev_test_sonarcloud_repo
sonar.organization=yhkl-dev

# This is the name and version displayed in the SonarCloud UI.
#sonar.projectName=test_sonarcloud_repo
#sonar.projectVersion=1.0

# Path is relative to the sonar-project.properties file. Replace "\" by "/" on Windows.
#sonar.sources=.

# Encoding of the source code. Default is default system encoding
#sonar.sourceEncoding=UTF-8
```

now we create a new branch and test sonarcloud 
![Img](./FILES/github_with_sonarqube.md/4d3191ae.png)

create new pull request
![Img](./FILES/github_with_sonarqube.md/3570ee8e.png)

you can see sonarcloud analyze your code now
![Img](./FILES/github_with_sonarqube.md/ffce751d.png)

![Img](./FILES/github_with_sonarqube.md/6b56beee.png)

check analyze result in your sonarcloud
![Img](./FILES/github_with_sonarqube.md/3afef84d.png)

And you can see the overview in your pull request as well
![Img](./FILES/github_with_sonarqube.md/71abb1d1.png)
