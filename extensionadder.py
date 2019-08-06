#!/usr/bin/python3

import sys # for argv
import magic # for mime types
import os # for path

# Available mime types. Most of them are stolen from:
# https://www.lifewire.com/file-extensions-and-mime-types-3469109
# It's not like I doubleckecked any of them. They may be inaccurate
# MP4, WebM, FLV and 3gp are detected no problemo
mimes = {
	'text/css': 'css',
	'text/html': 'html',
	'text/plain': 'txt',
	'text/richtext': 'rtx',
	'text/tsv': 'tsv',
	'text/csv': 'csv',
	'text/webwiewhtml': 'htt',
	'text/x-vcard': 'vcf',
	'image/bmp': 'bmp',
	'image/gif': 'gif',
	'image/jpeg': 'jpg',
	'image/png': 'png',
	'image/svg+xml': 'svg',
	'image/tiff': 'tiff',
	'image/x-icon': 'ico',
	'image/x-rgb': 'rgb',
	'audio/basic': 'snd',
	'audio/mid': 'mid',
	'audio/mpeg': 'mp3',
	'audio/x-aiff': 'aiff',
	'audio/x-mpegurl': 'm3u',
	'audio/x-pn-realaudio': 'ra',
	'audio/x-wav': 'wav',
	'video/mpeg': 'mpeg',
	'video/mp4': 'mp4',
	'video/webm': 'webm',
	'video/3gpp': '3gp',
	'video/quicktime': 'mov',
	'video/x-msvideo': 'avi',
	'video/x-sgi-movie': 'movie',
	'video/x-flv': 'flv',
	'application/hta': 'hta',
	'application/msword': 'doc',
	'application/pdf': 'pdf',
	'application/rtf': 'rtf',
	'application/x-dosexec': 'exe',
	'application/vnd.ms-excel': 'xlm',
	'application/vnd.ms-excel': 'xls',
	'application/vnd.ms-powerpoint': 'ppt',
	'application/x-compress': 'z',
	'application/x-compressed': 'tgz',
	'application/x-gtar': 'gtar',
	'application/x-gzip': 'gz',
	'application/x-latex': 'latex',
	'application/x-shockwave-flash': 'swf',
	'application/x-sh': 'sh',
	'application/x-tar': 'tar',
	'application/x-tex': 'tex',
	'application/x-troff-man': 'man',
	'application/zip': 'zip'
}

for path in range(1, len(sys.argv)): # Looping through every argument you give it
	filename = sys.argv[path]
	if os.path.splitext(filename)[1] == "": # Checking if a file has an extension
		if os.path.isdir(filename) == False: # Checking if it is a directory
			mime = magic.from_file(filename, mime=True) # Finding the mime type
			print("File %s has no extension. It seems to be %s." % (filename, mime))
			if mime in mimes: # Looking up mime in the dictionary above
				print("Renaming %s to %s ..." % (filename, filename + "." + mimes[mime]))
				os.rename(filename, filename + "." + mimes[mime])
				print("Success!\n")
			else:
				print("I have no idea what file is that. Skipping...\n")
		else:
			print("%s appears to be a directory. Skipping...\n" % filename)
	else:
		print("File %s already has an extension. Skipping...\n" % filename)
