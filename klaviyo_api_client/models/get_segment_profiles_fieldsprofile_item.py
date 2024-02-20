from enum import Enum


class GetSegmentProfilesFieldsprofileItem(str, Enum):
    CREATED = "created"
    EMAIL = "email"
    EXTERNAL_ID = "external_id"
    FIRST_NAME = "first_name"
    IMAGE = "image"
    JOINED_GROUP_AT = "joined_group_at"
    LAST_EVENT_DATE = "last_event_date"
    LAST_NAME = "last_name"
    LOCATION = "location"
    LOCATION_ADDRESS1 = "location.address1"
    LOCATION_ADDRESS2 = "location.address2"
    LOCATION_CITY = "location.city"
    LOCATION_COUNTRY = "location.country"
    LOCATION_IP = "location.ip"
    LOCATION_LATITUDE = "location.latitude"
    LOCATION_LONGITUDE = "location.longitude"
    LOCATION_REGION = "location.region"
    LOCATION_TIMEZONE = "location.timezone"
    LOCATION_ZIP = "location.zip"
    ORGANIZATION = "organization"
    PHONE_NUMBER = "phone_number"
    PREDICTIVE_ANALYTICS = "predictive_analytics"
    PREDICTIVE_ANALYTICS_AVERAGE_DAYS_BETWEEN_ORDERS = "predictive_analytics.average_days_between_orders"
    PREDICTIVE_ANALYTICS_AVERAGE_ORDER_VALUE = "predictive_analytics.average_order_value"
    PREDICTIVE_ANALYTICS_CHURN_PROBABILITY = "predictive_analytics.churn_probability"
    PREDICTIVE_ANALYTICS_EXPECTED_DATE_OF_NEXT_ORDER = "predictive_analytics.expected_date_of_next_order"
    PREDICTIVE_ANALYTICS_HISTORIC_CLV = "predictive_analytics.historic_clv"
    PREDICTIVE_ANALYTICS_HISTORIC_NUMBER_OF_ORDERS = "predictive_analytics.historic_number_of_orders"
    PREDICTIVE_ANALYTICS_PREDICTED_CLV = "predictive_analytics.predicted_clv"
    PREDICTIVE_ANALYTICS_PREDICTED_NUMBER_OF_ORDERS = "predictive_analytics.predicted_number_of_orders"
    PREDICTIVE_ANALYTICS_TOTAL_CLV = "predictive_analytics.total_clv"
    PROPERTIES = "properties"
    SUBSCRIPTIONS = "subscriptions"
    SUBSCRIPTIONS_EMAIL = "subscriptions.email"
    SUBSCRIPTIONS_EMAIL_MARKETING = "subscriptions.email.marketing"
    SUBSCRIPTIONS_EMAIL_MARKETING_CAN_RECEIVE_EMAIL_MARKETING = (
        "subscriptions.email.marketing.can_receive_email_marketing"
    )
    SUBSCRIPTIONS_EMAIL_MARKETING_CONSENT = "subscriptions.email.marketing.consent"
    SUBSCRIPTIONS_EMAIL_MARKETING_CONSENT_TIMESTAMP = "subscriptions.email.marketing.consent_timestamp"
    SUBSCRIPTIONS_EMAIL_MARKETING_CUSTOM_METHOD_DETAIL = "subscriptions.email.marketing.custom_method_detail"
    SUBSCRIPTIONS_EMAIL_MARKETING_DOUBLE_OPTIN = "subscriptions.email.marketing.double_optin"
    SUBSCRIPTIONS_EMAIL_MARKETING_LAST_UPDATED = "subscriptions.email.marketing.last_updated"
    SUBSCRIPTIONS_EMAIL_MARKETING_LIST_SUPPRESSIONS = "subscriptions.email.marketing.list_suppressions"
    SUBSCRIPTIONS_EMAIL_MARKETING_METHOD = "subscriptions.email.marketing.method"
    SUBSCRIPTIONS_EMAIL_MARKETING_METHOD_DETAIL = "subscriptions.email.marketing.method_detail"
    SUBSCRIPTIONS_EMAIL_MARKETING_SUPPRESSION = "subscriptions.email.marketing.suppression"
    SUBSCRIPTIONS_SMS = "subscriptions.sms"
    SUBSCRIPTIONS_SMS_MARKETING = "subscriptions.sms.marketing"
    SUBSCRIPTIONS_SMS_MARKETING_CAN_RECEIVE_SMS_MARKETING = "subscriptions.sms.marketing.can_receive_sms_marketing"
    SUBSCRIPTIONS_SMS_MARKETING_CONSENT = "subscriptions.sms.marketing.consent"
    SUBSCRIPTIONS_SMS_MARKETING_CONSENT_TIMESTAMP = "subscriptions.sms.marketing.consent_timestamp"
    SUBSCRIPTIONS_SMS_MARKETING_LAST_UPDATED = "subscriptions.sms.marketing.last_updated"
    SUBSCRIPTIONS_SMS_MARKETING_METHOD = "subscriptions.sms.marketing.method"
    SUBSCRIPTIONS_SMS_MARKETING_METHOD_DETAIL = "subscriptions.sms.marketing.method_detail"
    TITLE = "title"
    UPDATED = "updated"

    def __str__(self) -> str:
        return str(self.value)
