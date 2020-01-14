# Sample output (in any order/format):
#
# calculateClicksByDomain(counts) =>
# com:                     1340
# google.com:              900
# stackoverflow.com:       10
# overflow.com:            20
# yahoo.com:               410
# mail.yahoo.com:          60
# mobile.sports.yahoo.com: 10
# sports.yahoo.com:        50
# org:                     3
# wikipedia.org:           3
# en.wikipedia.org:        2
# m.wikipedia.org:         1
# mobile.sports:           1
# sports:                  1
# uk:                      1
# co.uk:                   1
# google.co.uk:            1
counts = ["900,google.com",
          "60,mail.yahoo.com",
          "10,mobile.sports.yahoo.com",
          "40,sports.yahoo.com",
          "300,yahoo.com",
          "10,stackoverflow.com",
          "20,overflow.com",
          "2,en.wikipedia.org",
          "1,m.wikipedia.org",
          "1,mobile.sports",
          "1,google.co.uk"]
class Solution(object):
    def subdomainVisits(self, counts):
        """
        :type cpdomains: List[str]
        :rtype: List[str]
        """
        out = {}
        for i in counts:
            w = i.split(',')
            out[w[1]]=w[0]

        _dict={}
        for domain in counts:
            domain=domain.split('.')
            print(domain)
            for i in xrange(1,len(domain)):
                # print(i)
                item='.'.join(domain[i:])
                if item in _dict:
                    _dict[item] += 1
                else:
                    _dict[item] = 1
        out.update(_dict)
        return out


s = Solution()
r = s.subdomainVisits(counts)
print(r)