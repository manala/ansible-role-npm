from __future__ import (absolute_import, division, print_function)
__metaclass__ = type

from ansible.plugins.lookup import LookupBase
from ansible.errors import AnsibleError

class LookupModule(LookupBase):

    def _do_flatten(self, terms, variables):

        ret = []
        for term in terms:
            term = self._check_list_of_one_list(term)

            if term == 'None' or term == 'null':
                # ignore undefined items
                break

            if isinstance(term, basestring):
                # convert a variable to a list
                term2 = listify_lookup_plugin_terms(term, templar=self._templar, loader=self._loader)
                # but avoid converting a plain string to a list of one string
                if term2 != [ term ]:
                    term = term2

            if isinstance(term, list):
                # if it's a list, check recursively for items that are a list
                term = self._do_flatten(term, variables)
                ret.extend(term)
            else:
                ret.append(term)

        return ret

    def run(self, terms, variables=None, **kwargs):

        ret = []

        #raise AnsibleError("lookup_plugin.lines(%s) returned %d" % (term, p.returncode))
        raise AnsibleError("boooo")

        for term in self._flatten(terms):
            if isinstance(term, basestring):
                ret.append({
                    'package': term
                })
            else:
                ret.append(term)

        return ret
