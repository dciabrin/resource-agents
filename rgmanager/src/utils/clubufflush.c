/*
  Copyright Red Hat, Inc. 2002
  Copyright Mission Critical Linux, 2000

  This program is free software; you can redistribute it and/or modify it
  under the terms of the GNU General Public License as published by the
  Free Software Foundation; either version 2, or (at your option) any
  later version.

  This program is distributed in the hope that it will be useful, but
  WITHOUT ANY WARRANTY; without even the implied warranty of
  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
  General Public License for more details.

  You should have received a copy of the GNU General Public License
  along with this program; see the file COPYING.  If not, write to the
  Free Software Foundation, Inc.,  675 Mass Ave, Cambridge, 
  MA 02139, USA.
*/
/** @file
 * Calls ioctl to invalidate/flush buffers on a given device.
 *
 * Author: Gregory P. Myrdal <Myrdal@MissionCriticalLinux.Com>
 *
 * invalidatebuffers.c
 */

/*
 * Version string that is filled in by CVS
 */
static const char *version __attribute__ ((unused)) = "$Revision$";

/*
 * System includes
 */
#include <unistd.h>
#include <stdio.h>
#include <syslog.h>
#include <linux/fs.h>
#include <string.h>
#include <sys/stat.h>
#include <errno.h>

#ifdef __NFDBITS
#undef __NFDBITS
#endif

#ifdef __FDMASK
#undef __FDMASK
#endif

#include <sys/types.h>
#include <fcntl.h>
#include <sys/ioctl.h>
#include <stdlib.h>
/*
 * Cluster includes
 */
#include <clulog.h>

/***************************************************************************
 *
 * Functions
 *
 ***************************************************************************/

/**
 * printUsage
 *
 * Print out usage string to stdout.
 */
static void
printUsage(char *progName)
{
	clulog_and_print(LOG_ERR, "Usage: %s [-h] [-f device]\n", progName);
}

/***************************************************************************
 *
 * Main
 *
 ***************************************************************************/
int
main(int argc, char **argv)
{
	int opt;
	uid_t uid;
	char *devicename = (char *)NULL;
	int fd;

	uid=getuid();
	if (uid)
	  {
	    clulog_and_print(LOG_ERR, "%s should only be run as user root\n",
	            argv[0]);
	    exit(1);
	  }

	while ((opt = getopt(argc, argv, "f:h")) != -1)
	  {
	    switch (opt)
	      {
              case 'f':			// stop services
	        devicename = strdup(optarg);
	        break;

              case 'h':			// command line help
                printUsage(argv[0]);
	        exit(0);

              default:			// unknown option
                printUsage(argv[0]);     
	        exit(0);
	      }
	  }

	if (devicename == (char *)NULL)
	  {
	    printUsage(argv[0]);
	    exit(1);
	  }

	fd = open(devicename, O_RDONLY, 0);

	if (fd < 0)
	  {
	    clulog_and_print(LOG_ERR, "Cannot open %s for flushing: %s\n",
	            devicename, strerror(errno));
	    exit(1);
	  }

	if (ioctl(fd, BLKFLSBUF, 0) < 0)
	  {
	    clulog_and_print(LOG_ERR, "Cannot flush %s: %s\n",
	            devicename, strerror(errno));
	    exit(1);
	  }
	free(devicename);
	close(fd);           

	exit(0);
}
