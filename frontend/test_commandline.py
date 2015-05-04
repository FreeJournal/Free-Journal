import unittest
import subprocess
import config


def run_with_timeout(command, timeout):
    return subprocess.check_output(
        "(timeout " + str(timeout) + " " + command + "); exit 0",
        stderr=subprocess.STDOUT, shell=True)


class TestCommandLine(unittest.TestCase):

    def test_getdocfile(self):
        # Download sample file
        out = run_with_timeout("./freejournal_cli.py getdoc " +
                               "CHK@XNpzyZhvxvkgIBgYuZzeJTSpRBPnR0VibpISMc8rHV4,4rsKU2MpJzpQxr91fPTV-wGpd14o~ns3hjLi0HMtwFI,AAMA--8 /tmp/1-freejournal",
                               10)

        self.assertFalse("traceback" in out.lower())
        self.assertFalse("error" in out.lower())
        # self.assertFalse("exception" in out.lower())
        file_output = open("/tmp/1-freejournal").read()
        self.assertTrue("iteration meeting" in file_output.lower())

    def test_listcollections(self):
        list_collections = run_with_timeout(
            "./freejournal_cli.py listcollections", 10)

        self.assertFalse("traceback" in list_collections.lower())
        self.assertFalse("error" in list_collections.lower())
        self.assertFalse("exception" in list_collections.lower())
        self.assertTrue(
            "available collections, cached locally" in list_collections.lower())

    def test_put_list_show_publish_collections(self):
        # List all collections, store output
        list_collections_original = run_with_timeout(
            "./freejournal_cli.py listcollections", 10)

        self.assertFalse("traceback" in list_collections_original.lower())
        self.assertFalse("error" in list_collections_original.lower())
        self.assertFalse("exception" in list_collections_original.lower())
        self.assertTrue(
            "available collections, cached locally" in list_collections_original.lower())

        # Add new collection to local cache
        out = run_with_timeout(
            './freejournal_cli.py putcollection whee "This is a TEST" "nothing to see here" "nothing,to" btc123', 10)

        self.assertFalse("traceback" in out.lower())
        self.assertFalse("error" in out.lower())
        self.assertFalse("exception" in out.lower())
        self.assertTrue("collection inserted with address/id" in out.lower())

        # Attempt to grab inserted collection ID
        for line in out.splitlines():
            if "/ID" in line:
                inserted_collection_id = line[line.find("/ID") + 4:].strip()

        print "Inserted ID: " + inserted_collection_id

        # Make sure new collection is added (list collections output longer than before, basic sanity checks)
        # List all collections, store output
        list_collections_new = run_with_timeout(
            "./freejournal_cli.py listcollections", 10)

        self.assertFalse("traceback" in list_collections_new.lower())
        self.assertFalse("error" in list_collections_new.lower())
        self.assertFalse("exception" in list_collections_new.lower())
        self.assertTrue(
            "available collections, cached locally" in list_collections_new.lower())

        self.assertTrue(len(list_collections_new.splitlines())
                        > len(list_collections_original.splitlines()))

        # Check that new collection title, document list appears
        self.assertTrue("document list" in list_collections_new.lower())
        self.assertTrue("This is a TEST" in list_collections_new)

        # Try publishing the collection
        upload_output = run_with_timeout(
            "./freejournal_cli.py publishcollection whee " + inserted_collection_id, 60)

        self.assertFalse("traceback" in upload_output.lower())
        self.assertFalse("error" in upload_output.lower())
        self.assertFalse("exception" in upload_output.lower())
        self.assertTrue("published success" in upload_output.lower())

    def test_fail_publish_collection(self):
        # Check collection with invalid/uncached ID
        out = run_with_timeout(
            "./freejournal_cli.py publishcollection 59 59", 10)

        self.assertTrue("not found in local cache" in out.lower())
        self.assertFalse("published" in out.lower())

    def test_webapp(self):
        out = run_with_timeout("./freejournal_cli.py webapp", 5)

        # Check that process was spawned, is listening on correct port
        self.assertTrue("running on" in out.lower())
        self.assertTrue(":" + str(config.WEBAPP_PORT) in out)
        # Check for general exceptions
        self.assertFalse("exception" in out.lower())
        # Ensure no extra output emitted and no Python exception occured
        self.assertTrue(
            len(out.splitlines()) < 3 and not "traceback" in out.lower())

    def test_manually(self):
        # Tests to run manually, as functionality is not amenable to testing
        # (extremely long running processes & GUI)
        print "Manually test: "
        print "putdoc, installer, uploader, keepalive"

suite = unittest.TestLoader().loadTestsFromTestCase(TestCommandLine)
unittest.TextTestRunner(verbosity=2).run(suite)
