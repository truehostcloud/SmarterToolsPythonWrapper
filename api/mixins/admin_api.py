from abc import abstractmethod
from typing import Dict, Optional, Protocol


class SMAPIMixin(Protocol):
    """Mixin for SMAPI"""

    @abstractmethod
    def _get(self, endpoint: str, path_params="") -> Dict:
        """Make a GET request to the SMAPI"""
        raise NotImplementedError

    @abstractmethod
    def _post(self, endpoint: str, data: Optional[Dict] = None, path_params="") -> Dict:
        """Make a POST request to the SMAPI"""
        raise NotImplementedError


# pylint: disable=abstract-method
# Reason: https://github.com/pylint-dev/pylint/issues/3098#issuecomment-529351894
class AdminAPIMixin(SMAPIMixin, Protocol):
    """Mixin for admin API"""

    def system_update_domain_settings(self, domain: str, data: Dict):
        """Update domain settings on cloudoon email server"""
        payload = {"domainSettings": data}
        return self._post(f"/api/v1/settings/sysadmin/domain/{domain}", payload)

    def system_add_domain(self, data: Dict):
        """Create domain on cloudoon email server"""
        return self._post("/api/v1/settings/sysadmin/domain-put", data)

    def system_delete_domain(self, domain: str):
        """Delete domain on cloudoon email server"""
        return self._post(f"/api/v1/settings/sysadmin/domain-delete/{domain}/true")

    def system_suspend_domain(self, domain: str):
        """Suspend domain on cloudoon email server"""
        payload = {"isEnabled": False}
        return self.system_update_domain_settings(domain, payload)

    def system_unsuspend_domain(self, domain: str):
        """Unsuspend domain on cloudoon email server"""
        payload = {"isEnabled": True}
        return self.system_update_domain_settings(domain, payload)

    def system_get_login_token(self, domain: str, username: str, **kwargs):
        """
        Get login from cloudoon email server.

        :param domain: The domain name of the email server. (str)
        :param username: The username of the user. (str)
        :param is_system_admin: A flag indicating whether the user is a system admin. (bool)

        :return: A dictionary containing the following keys:
            - "autoLoginToken": A token that can be used for auto login.
                                This token is valid for 1 minute. (str)
            - "autoLoginUrl": A URL containing the auto login token that can
                                be used to login. This URL is valid for 1 minute. (str)
            - "success": A boolean indicating if the function call succeeded. (bool)
            - "resultCode": An enumeration representing the HTTP status code. (enum)
            - "message": If success is False, this field provides information
                        about the failure reason. (str)
            - "debugInfo": Additional information related to the function call. (str)
        """
        is_system_admin = kwargs.pop("is_system_admin", False)
        payload = {
            "username": username,
            "domain": domain,
            "isSystemAdmin": is_system_admin,
        }

        return self._post("/api/v1/auth/retrieve-login-token", payload)

    def system_get_auto_login_url(self, domain: str, username: str, *args, **kwargs):
        """Get auto login url from cloudoon email server"""
        response = self.system_get_login_token(
            *args, domain=domain, username=username, **kwargs
        )
        return response.get("autoLoginUrl")
