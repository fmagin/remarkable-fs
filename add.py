

#c = root.new_collection("TestCollection")
#c.save()
import sys
if len(sys.argv) > 1:
    from remarkable_fs.connection import LocalConnection
    from remarkable_fs.documents import DocumentRoot

    conn = LocalConnection()
    root = DocumentRoot(conn)
    root.add_file(sys.argv[1])
else:
    print("requires file arg")
#root.add_file("/home/root/road_to_infinity.pdf")
#d.children
