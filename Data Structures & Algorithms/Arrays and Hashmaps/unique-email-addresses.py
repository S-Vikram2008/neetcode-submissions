class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        
        unique=set()

        for i in emails:
            local=i.split('@')[0] # Getting local address
            domain=i.split('@')[1] # Getting domain address

            localaddr='' # For storing final local name without . and +

            # Loop for checking '.' and '+' in local name
            for i in local:
                if i=='.':
                    pass
                elif i=='+':
                    break
                else:
                    localaddr+=i
            
            # Merging localname and @ and domain name to form complete email
            email=localaddr+'@'+domain
            # Since a unique is a set we add every email to a set to avoid repetitive emails
            unique.add(email)
        
        # Finally we return the length of the unique set to get number of unique emails
        return len(unique)


