from pprint import pprint

import requests

from config import Config
import json

from utils import Utils


class Gitlab:
    def __init__(self):
        config = Config()
        cfg = config.parseConfig()
        self.gitlabURL = cfg["gitlab"]["url"]
        self.gitlabToken = cfg["gitlab"]["token"]
        self.apiVersion = cfg["gitlab"]["apiVersion"]

    def _callURL(self, path):
        resp = requests.get(f"{self.gitlabURL}/api/{self.apiVersion}/{path}",
                            headers={"PRIVATE-TOKEN": self.gitlabToken})
        if resp.status_code != 200:
            Utils.dump(resp)
            resp = {"status_code": resp.status_code, "reason": resp.reason, "message": resp.text}
            return json.dumps(resp, indent=4)
        else:
            return json.loads(resp.content)

    def getLatestPipeline(self, project_id):
        resp = self._callURL(f"/projects/{project_id}/pipelines/latest")
        return resp

    def getAllProjects(self):
        resp = self._callURL(f"/projects")
        return resp

    def getProject(self, project_id):
        resp = self._callURL(f"/projects/{project_id}")
        return resp

    def getPipelines(self, project_id):
        resp = self._callURL(f"/projects/{project_id}/pipelines")
        return resp
