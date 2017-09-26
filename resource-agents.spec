#
# All modifications and additions to the file contributed by third parties
# remain the property of their copyright owners, unless otherwise agreed
# upon. The license for this file, and modifications and additions to the
# file, is the same license as for the pristine package itself (unless the
# license for the pristine package is not an Open Source License, in which
# case the license is the MIT License). An "Open Source License" is a
# license that conforms to the Open Source Definition (Version 1.9)
# published by the Open Source Initiative.
#






# 
# Since this spec file supports multiple distributions, ensure we
# use the correct group for each.
#

## Whether this platform defaults to using systemd as an init system
## (needs to be evaluated prior to BuildRequires being enumerated and
## installed as it's intended to conditionally select some of these, and
## for that there are only few indicators with varying reliability:
## - presence of systemd-defined macros (when building in a full-fledged
##   environment, which is not the case with ordinary mock-based builds)
## - systemd-aware rpm as manifested with the presence of particular
##   macro (rpm itself will trivially always be present when building)
## - existence of /usr/lib/os-release file, which is something heavily
##   propagated by systemd project
## - when not good enough, there's always a possibility to check
##   particular distro-specific macros (incl. version comparison)
%define systemd_native (%{?_unitdir:1}%{?!_unitdir:0}%{nil \
  } || %{?__transaction_systemd_inhibit:1}%{?!__transaction_systemd_inhibit:0}%{nil \
  } || %(test -f /usr/lib/os-release; test $? -ne 0; echo $?))

%global upstream_prefix ClusterLabs-resource-agents
%global upstream_version 5434e96

%global sap_script_prefix sap_redhat_cluster_connector
%global sap_hash 6353d27

# determine the ras-set to process based on configure invokation
%bcond_with rgmanager
%bcond_without linuxha

Name:		resource-agents
Summary:	Open Source HA Reusable Cluster Resource Scripts
Version:	3.9.5
Release:	105%{?dist}.0.0.rdo1
License:	GPLv2+, LGPLv2+ and ASL 2.0
URL:		https://github.com/ClusterLabs/resource-agents
%if 0%{?fedora} || 0%{?centos_version} || 0%{?rhel}
Group:		System Environment/Base
%else
Group:		Productivity/Clustering/HA
%endif
Source0:	http://people.redhat.com/mbaldess/rpms/container-repo/sources/resource-agents/%{upstream_prefix}-%{upstream_version}.tar.gz
Source1:	http://people.redhat.com/mbaldess/rpms/container-repo/sources/resource-agents/%{sap_script_prefix}-%{sap_hash}.tar.gz
Patch1:		bz984054.patch		
Patch2:		bz884164-multi-lib-fixes.patch
Patch3:		bz10005924-default-apache-config.patch
Patch4:		bz799065-apache-simple-monitor.patch
Patch5:		fix-LVM-clvmd-retry.patch
Patch6:		bz917806-oracle-tns-admin.patch
Patch7:		bz917681-VirtualDomain-heartbeat-updates.patch
Patch8:		bz917681_nodename_fixes.patch
Patch9:		bz1014641-VirtualDomain-syntax-error.patch 
Patch10:	bz917681-VirtualDomain-heartbeat-updates_v2.patch
Patch11:	bz1016140-start-predefined-domains.patch
Patch12:	bz917681-ipv6-send_ua-fix.patch
Patch13:	bz917681-ocft_fedora_supported_test_cases.patch
Patch14:	bz1033016-nfsserver-missing-etab.patch
Patch15:	bz917681-slapd-heartbeat-updates.patch
Patch16:	bz917681-tomcat-heartbeat-updates.patch
Patch17:	bz1029061-virtualdomain-parse-error.patch 
Patch18:	bz1064512-clvmd-agent.patch
Patch19:	bz1060367-vm-monitor-wo-libvirtd.patch
Patch20:	bz1060367-vm-monitor-wo-libvirtd_2.patch
Patch21:	bz1116166-galera-agent.patch
Patch22:	bz1091101-nfs-updates.patch
Patch23:	bz1091101-nfs-error-msg-fix.patch
Patch24:	bz1091101-nfs-rquotad-port-option-fix.patch
Patch25:	bz1083041-virtual-domain-monitor-lxc-fix.patch
Patch26:	bz1083231-fs-wait-module-load.patch
Patch27:	bz1097593-LVM-warn-lvmetad.patch
Patch28:	bz1105655-virtualdomain-restore-start-stop-default-timeout.patch
Patch29:	bz1128933-IPaddr2-exit-reason-support.patch
Patch30:	bz1128933-VirtualDomain-exit-reason-support.patch
Patch31:	bz1128933-binary-check-exit-reason-support.patch
Patch32:	bz1128933-exportfs-exit-reason-support.patch
Patch33:	bz1128933-introducing-exit-reason-support.patch
Patch34:	bz1128933-nfsnotify-exit-reason-support.patch
Patch35:	bz1128933-nfssserver-exit-reason-support.patch
Patch36:	bz773395-clvm-autoset-locking-type.patch
Patch37:	bz1058102-man-page-updates.patch
Patch38:	bz1118029-iscsi-agents.patch
Patch39:	bz1122285-ethmonitor-infiniband.patch
Patch40:	bz1128933-exit-reason-string-updates.patch
Patch41:	bz1095944-safe-umount-option.patch
Patch42:	bz1118029_iscsi_syntax_fix.patch
Patch43:	bz1138871_mysql_stop_fix.patch
Patch44:	bz1116166-Low-galera-do-not-advertise-notify-in-the-usage.patch
Patch45:	bz1116166-Low-galera-be-very-generous-in-the-promotion-timeout.patch
Patch46:	bz1116166-galera-do-not-ignore-check_password.patch
Patch47:	bz1128933-Fix-shellfuncs-fix-syntax-error-caused-by-exit_reaso.patch
Patch48:	bz1128933-Fix-ocf_exit_reason-implicit-format-string-s-for-sin.patch
Patch49:	bz1128933-Fix-ha_log-drop-global-__ha_log_ignore_stderr_once-h.patch
Patch50:	bz1138871-avoid-check-binary-in-validate.patch
Patch51:	bz1138871-mysql-error-validation-fails-monitor.patch
Patch52:	bz1135026-introducing-docker-agent.patch
Patch53:	bz1135026-docker-stop-fix.patch
Patch54:	bz1135026-docker-name-arg.patch
Patch55:	bz1135026-docker-monitor_cmd-arg.patch
Patch56:	bz1135026-docker-handle-invalid-monitor-cmd.patch
Patch57:	bz1118029-iscsi-remove-write-back.patch
Patch58:	rabbitmq-cluster.patch
Patch59:	bz1189187-redis-agent.patch
Patch60:	bz1170376-galera-no-readonly.patch
Patch61:	bz1198681-clvm-activate-vgs-option.patch
Patch62:	bz1200756-ipsrcaddr-misconfig.patch
Patch63:	bz773399-netmast-error.patch
Patch64:	bz1059988-db2-support.patch
Patch65:	bz1077888-ctdb-updates.patch
Patch66:	bz1171162-clvmd-opt-fix.patch
Patch67:	bz1183136-nginx-support.patch
Patch68:	bz1213971-ethmon-opt.patch
Patch69:	nfs-fixes-update.patch
Patch70:	bz1160365-iface-vlan.patch.patch
Patch71:	bz1214781-lvm-partial-activation-fix.patch.patch
Patch72:	bz1223615-apache-includes-fix.patch.patch
Patch73:	NovaCompute.patch
Patch74:	bz1214360-NovaCompute-update1.patch.patch
Patch75:	bz1227293-dhcpd-chroot-fix.patch.patch
Patch76:	bz1231032-redis-update.patch.patch
Patch77:	bz1232376-oracle-agent-update.diff
Patch78:	bz1168251-SAPHana-agents.patch
Patch79:	bz1168251-SAPHana-agents-update.patch
Patch80:	bz1168251-SAPHana-agents-update2.patch
Patch81:	bz1168251-SAPHana-agents-update3.patch
Patch82:	bz1168251-SAPHana-agents_update4.patch
Patch83:	bz1251484-redis-client-passwd-support.patch
Patch84:	bz1282723-novacompute-novaevacuate-fix-evacute-typo.patch
Patch85:	bz1287303-novaevacuate-invoke-off-action.patch
Patch86:	bz1126073-1-nfsserver-fix-systemd-status-detection.patch
Patch87:	bz1299404-galera-custom-host-port.patch
Patch88:	bz1247303-rabbitmq-cluster-forget-stopped-cluster-nodes.patch
Patch89:	bz1249430-1-tomcat-fix-selinux-enforced.patch
Patch90:	bz1250728-send_arp-fix-buffer-overflow-on-infiniband.patch
Patch91:	bz1263348-mysql-tmpfile-leak.patch
Patch92:	bz1242181-virtualdomain-migrate_options.patch
Patch93:	bz1242558-virtualdomain-may-remove-config-file.patch
Patch94:	bz1301189-virtualdomain-fix-locale.patch
Patch95:	bz1276699-ipaddr2-use-ipv6-dad-for-collision-detection.patch
Patch96:	bz1212632-nagios.patch
Patch97:	bz1303803-Backup-and-restore-rabbitmq-users-during-resource-re.patch
Patch98:	bz1265527-sap_redhat_cluster_connector-hostnames-with-dash.patch
Patch99:	bz1287314-novaevacuate-simplify-nova-check.patch
Patch100:	bz1303037-1-portblock.patch
Patch101:	bz1284526-galera-crash-recovery.patch
Patch102:	bz1284526-galera-heuristic-recovered.patch
Patch103:	bz1284526-galera-no-grastate.patch
Patch104:	bz1289107-saphana-mcos-support.patch
Patch105:	bz1296406-virtualdomain-migration_speed-migration_downtime.patch
Patch106:	bz1307160-virtualdomain-fix-unnecessary-error-when-probing-nonexistent-domain.patch
Patch107:	bz1317578-oralsnr-fails-if-username-is-longer-than-8-chars.patch
Patch108:	bz1318985-oracle-fix-unable-to-start-because-of-ORA-01081.patch
Patch109:	bz1325453-nfsserver-var-lib-nfs-fix.patch
Patch110:	bz1320783-nova-compute-wait-fix-invalid-hostname-issue.patch
Patch111:	bz1328018-garbd-Introduces-garbd-resource-agent.patch
Patch112:	bz1337109-tickle_tcp-fix.patch
Patch113:	bz1337615-nfsserver-rpcpipefs_dir.patch
Patch114:	bz1337124-mysql-use-replication_port-parameter.patch
Patch115:	bz1328386-1-oracle-monprofile-container-databases.patch
Patch116:	bz1342478-rabbitmq-cluster-return-code-69-not-running.patch
Patch117:	bz1343905-1-rabbitmq-cluster-dump-restore-users-3.6.x.patch
Patch118:	bz1343905-2-rabbitmq-cluster-dump-restore-users-3.6.x.patch
Patch119:	bz1343905-3-rabbitmq-cluster-dump-restore-users-3.6.x.patch
Patch120:	bz1126073-2-nfsserver-fix-systemd-status-detection.patch
Patch121:	bz1358895-oracle-fix-monprofile.patch
Patch122:	bz1343905-rabbitmq-automatic-cluster-recovery.patch
Patch123:	bz1328386-2-oracle-monprofile-container-databases.patch
Patch124:	bz1328386-3-oracle-monprofile-container-databases.patch
Patch125:	bz1303037-2-portblock.patch
Patch126:	bz1249430-2-tomcat-fix-selinux-enforced.patch
Patch127:	bz1387491-nfsserver-keep-options.patch
Patch128:	bz1390974-redis-fix-selinux-permissions.patch
Patch129:	bz1305549-redis-notify-clients-of-master-being-demoted.patch
Patch130:	bz1305549-nova-compute-wait-nova-compute-unfence.patch
Patch131:	bz1360768-galera-prevent-promote-after-demote.patch
Patch132:	bz1376588-iSCSITarget-properly-create-portals-for-lio-t.patch
Patch133:	bz1384955-nfsserver-dont-stop-rpcbind.patch
Patch134:	bz1387363-Filesystem-submount-check.patch
Patch135:	bz1388854-delay-change-startdelay.patch
Patch136:	bz1391470-galera-last-commit-fix-for-mariadb-10.1.18.patch
Patch137:	bz1391580-portblock-return-success-on-stop-with-invalid-ip.patch
Patch138:	bz1402370-portblock-wait.patch
Patch139:	bz1406152-exportfs-ipv6-fix.patch
Patch140:	bz1395142-1-update-saphana-saphanatopology.patch
Patch141:	bz1395142-2-update-saphana-saphanatopology.patch
Patch142:	bz1260713-1-sapdatabase-process-count-suser.patch
Patch143:	bz1260713-2-sapdatabase-process-count-suser.patch
Patch144:	bz1397393-rabbitmq-cluster-reset-mnesia-before-join.patch
Patch145:	bz1392432-LVM-partial_activation-fix.patch
Patch146:	bz1159328-LVM-check_writethrough.patch
Patch147:	bz1359252-clvm-remove-reload-action.patch
Patch148:	bz1389300-iSCSILogicalUnit-IPv6-support.patch
Patch149:	bz1400172-IPsrcaddr-fix-duplicate-routes.patch
Patch150:	bz1420565-pgsql-dont-use-crm_failcount.patch
Patch151:	bz1427611-ocf_log-use-same-log-format-as-pacemaker.patch
Patch152:	bz1430304-NodeUtilization.patch
Patch153:	bz1430385-iSCSILogicalUnit-iSCSITarget-concurrent-safe.patch
Patch154:	bz1434351-IPaddr2-send-arp-monitor-action.patch
Patch155:	bz1435171-named-add-support-for-rndc-options.patch
Patch156:	bz1077888-CTDB-fix-logging.patch
Patch157:	bz1393189-1-IPaddr2-detect-duplicate-IP.patch
Patch158:	bz1393189-2-IPaddr2-detect-duplicate-IP.patch
Patch159:	bz1408656-ethmonitor-monitor-interface-without-ip.patch
Patch160:	bz1411225-oraasm.patch
Patch161:	bz1435982-rabbitmq-cluster-pacemaker-remote.patch
Patch162:	bz1380405-send_arp-usage.patch
Patch163:	bz1427574-DB2-fix-HADR-DB2-V98-or-later.patch
Patch164:	bz1342376-rabbitmq-cluster-backup-and-restore-users-policies.patch
Patch165:	bz1445861-IPaddr2-IPv6-add-preferred_lft-parameter.patch
Patch166:	bz1316130-systemd-drop-in-clvmd-LVM.patch
Patch167:	bz1449681-1-saphana-saphanatopology-update-0.152.21.patch
Patch168:	bz1451097-1-galera-fix-bootstrap-when-cluster-has-no-data.patch
Patch169:	bz1451097-2-galera-fix-bootstrap-when-cluster-has-no-data.patch
Patch170:	bz1451097-3-galera-fix-bootstrap-when-cluster-has-no-data.patch
Patch171:	bz1452049-docker-create-directories.patch
Patch172:	bz1454699-LVM-status-check-for-missing-VG.patch
Patch173:	bz1451933-LVM-update-metadata-on-start-relocate.patch
Patch174:	bz1451933-LVM-warn-when-cache-mode-not-writethrough.patch
Patch175:	bz1449681-2-saphana-saphanatopology-update-0.152.21.patch
Patch176:	bz1342376-2-rabbitmq-cluster-backup-and-restore-users-policies.patch
Patch177:	bz1342376-3-rabbitmq-cluster-backup-and-restore-users-policies.patch
Patch178:	bz1493915-1-support-per-host-per-bundle-attribs.patch
Patch179:	bz1493915-2-support-per-host-per-bundle-attribs.patch

Obsoletes:	heartbeat-resources <= %{version}
Provides:	heartbeat-resources = %{version}

## Setup/build bits
BuildRoot: %(mktemp -ud %{_tmppath}/%{name}-%{version}-%{release}-XXXXXX)

# Build dependencies
BuildRequires: automake autoconf pkgconfig
BuildRequires: perl python-devel
BuildRequires: libxslt glib2-devel
BuildRequires: which

%if %{systemd_native}
BuildRequires: pkgconfig(systemd)
%endif

%if 0%{?fedora} || 0%{?centos_version} || 0%{?rhel}
#BuildRequires: cluster-glue-libs-devel
BuildRequires: docbook-style-xsl docbook-dtds
%if 0%{?rhel} == 0
BuildRequires: libnet-devel
%endif
%endif

## Runtime deps
# system tools shared by several agents
Requires: /bin/bash /bin/grep /bin/sed /bin/gawk
Requires: /bin/ps /usr/bin/pkill /bin/hostname /bin/netstat
Requires: /usr/sbin/fuser /bin/mount

# Filesystem / fs.sh / netfs.sh
Requires: /sbin/fsck
Requires: /usr/sbin/fsck.ext2 /usr/sbin/fsck.ext3 /usr/sbin/fsck.ext4
Requires: /usr/sbin/fsck.xfs
Requires: /sbin/mount.nfs /sbin/mount.nfs4 /usr/sbin/mount.cifs

# IPaddr2
Requires: /sbin/ip

# LVM / lvm.sh
Requires: /usr/sbin/lvm

# nfsserver / netfs.sh
Requires: /usr/sbin/rpc.nfsd /sbin/rpc.statd /usr/sbin/rpc.mountd

# rgmanager
%if %{with rgmanager}
# ip.sh
Requires: /usr/sbin/ethtool
Requires: /sbin/rdisc /usr/sbin/arping /bin/ping /bin/ping6

# nfsexport.sh
Requires: /sbin/findfs
Requires: /sbin/quotaon /sbin/quotacheck
%endif

## Runtime dependencies required to guarantee heartbeat agents
## are functional
%if %{with linuxha}
# ethmonitor requires the bc calculator
Requires: bc
# tools needed for Filesystem resource
Requires: psmisc
# Tools needed for clvm resource. 
Requires: procps-ng
%endif

%description
A set of scripts to interface with several services to operate in a
High Availability environment for both Pacemaker and rgmanager
service managers.

%ifarch x86_64 ppc64le
%package sap
License:      GPLv2+
Summary:      SAP cluster resource agents and connector script
%if 0%{?fedora} || 0%{?centos_version} || 0%{?rhel}
Group:		System Environment/Base
%else
Group:		Productivity/Clustering/HA
%endif
Requires:     %{name} = %{version}-%{release}
Requires:	perl

%description sap
The SAP resource agents and connector script interface with 
Pacemaker to allow SAP instances to be managed in a cluster
environment.
%endif

%ifarch x86_64 ppc64le
%package sap-hana
License:      GPLv2+
Summary:      SAP HANA cluster resource agents
%if 0%{?fedora} || 0%{?centos_version} || 0%{?rhel}
Group:		System Environment/Base
%else
Group:		Productivity/Clustering/HA
%endif
Requires:     %{name} = %{version}-%{release}
Requires:	perl

%description sap-hana
The SAP HANA resource agents interface with  Pacemaker to allow
SAP instances to be managed in a cluster environment.
%endif

%prep
%if 0%{?suse_version} == 0 && 0%{?fedora} == 0 && 0%{?centos_version} == 0 && 0%{?rhel} == 0
%{error:Unable to determine the distribution/version. This is generally caused by missing /etc/rpm/macros.dist. Please install the correct build packages or define the required macros manually.}
exit 1
%endif
%setup -q -n %{upstream_prefix}-%{upstream_version}
%setup -a 1 -n %{upstream_prefix}-%{upstream_version}
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1
%patch5 -p1
%patch6 -p1
%patch7 -p1
%patch8 -p1
%patch9 -p1
%patch10 -p1
%patch11 -p1
%patch12 -p1 -b .bz917681.1
%patch13 -p1 -b .bz917681.1
%patch14 -p1
%patch15 -p1
%patch16 -p1
%patch17 -p1
%patch18 -p1
%patch19 -p1
%patch20 -p1
%patch21 -p1
%patch22 -p1
%patch23 -p1
%patch24 -p1
%patch25 -p1
%patch26 -p1
%patch27 -p1
%patch28 -p1
%patch29 -p1
%patch30 -p1
%patch31 -p1
%patch32 -p1
%patch33 -p1
%patch34 -p1
%patch35 -p1
%patch36 -p1
%patch37 -p1
%patch38 -p1
%patch39 -p1
%patch40 -p1
%patch41 -p1
%patch42 -p1
%patch43 -p1
%patch44 -p1
%patch45 -p1
%patch46 -p1
%patch47 -p1
%patch48 -p1
%patch49 -p1
%patch50 -p1
%patch51 -p1
%patch52 -p1
%patch53 -p1
%patch54 -p1
%patch55 -p1
%patch56 -p1
%patch57 -p1
%patch58 -p1
%patch59 -p1
%patch60 -p1
%patch61 -p1
%patch62 -p1
%patch63 -p1
%patch64 -p1
%patch65 -p1
%patch66 -p1
%patch67 -p1
%patch68 -p1
%patch69 -p1
%patch70 -p1
%patch71 -p1
%patch72 -p1
%patch73 -p1
%patch74 -p1
%patch75 -p1
%patch76 -p1
%patch77 -p1
%patch78 -p1
%patch79 -p1
%patch80 -p1
%patch81 -p1
%patch82 -p1
%patch83 -p1
%patch84 -p1
%patch85 -p1
%patch86 -p1
%patch87 -p1
%patch88 -p1
%patch89 -p1
%patch90 -p1
%patch91 -p1
%patch92 -p1
%patch93 -p1
%patch94 -p1
%patch95 -p1
%patch96 -p1
%patch97 -p1
%patch98 -p1
%patch99 -p1
%patch100 -p1
%patch101 -p1
%patch102 -p1
%patch103 -p1
%patch104 -p1
%patch105 -p1
%patch106 -p1
%patch107 -p1
%patch108 -p1
%patch109 -p1
%patch110 -p1
%patch111 -p1 -F2
%patch112 -p1
%patch113 -p1
%patch114 -p1
%patch115 -p1
%patch116 -p1
%patch117 -p1
%patch118 -p1
%patch119 -p1 -F2
%patch120 -p1
%patch121 -p1
%patch122 -p1
%patch123 -p1
%patch124 -p1 -F2
%patch125 -p1
%patch126 -p1
%patch127 -p1
%patch128 -p1
%patch129 -p1
%patch130 -p1
%patch131 -p1 -F1
%patch132 -p1
%patch133 -p1
%patch134 -p1
%patch135 -p1
%patch136 -p1
%patch137 -p1
%patch138 -p1
%patch139 -p1
%patch140 -p1
%patch141 -p1
%patch142 -p1
%patch143 -p1
%patch144 -p1
%patch145 -p1
%patch146 -p1
%patch147 -p1
%patch148 -p1
%patch149 -p1
%patch150 -p1
%patch151 -p1
%patch152 -p1
%patch153 -p1
%patch154 -p1
%patch155 -p1
%patch156 -p1
%patch157 -p1
%patch158 -p1
%patch159 -p1
%patch160 -p1
%patch161 -p1
%patch162 -p1 -F2
%patch163 -p1
%patch164 -p1
%patch165 -p1
%patch166 -p1
%patch167 -p1
%patch168 -p1
%patch169 -p1
%patch170 -p1
%patch171 -p1
%patch172 -p1
%patch173 -p1
%patch174 -p1
%patch175 -p1
%patch176 -p1
%patch177 -p1
%patch178 -p1
%patch179 -p1 -F2

%build
if [ ! -f configure ]; then
	./autogen.sh
fi

chmod 755 heartbeat/galera
chmod 755 heartbeat/garbd
chmod 755 heartbeat/mysql-common.sh
chmod 755 heartbeat/nagios
chmod 755 heartbeat/nfsnotify
chmod 755 heartbeat/docker
chmod 755 heartbeat/rabbitmq-cluster
chmod 755 heartbeat/redis
chmod 755 heartbeat/iface-vlan
chmod 755 heartbeat/nova-compute-wait
chmod 755 heartbeat/oraasm
chmod 755 heartbeat/NovaEvacuate
chmod 755 heartbeat/NodeUtilization
chmod 755 heartbeat/SAPHana
chmod 755 heartbeat/SAPHanaTopology

%if 0%{?fedora} >= 11 || 0%{?centos_version} > 5 || 0%{?rhel} > 5
CFLAGS="$(echo '%{optflags}')"
%global conf_opt_fatal "--enable-fatal-warnings=no"
%else
CFLAGS="${CFLAGS} ${RPM_OPT_FLAGS}"
%global conf_opt_fatal "--enable-fatal-warnings=yes"
%endif

%if %{with rgmanager}
%global rasset rgmanager
%endif
%if %{with linuxha}
%global rasset linux-ha
%endif
%if %{with rgmanager} && %{with linuxha}
%global rasset all
%endif

export CFLAGS

chmod 755 heartbeat/clvm

%configure \
	%{conf_opt_fatal} \
%if %{defined _unitdir}
    --with-systemdsystemunitdir=%{_unitdir} \
%endif
	--with-pkg-name=%{name} \
	--with-ras-set=%{rasset} \
	--with-ocft-cases=fedora

%if %{defined jobs}
JFLAGS="$(echo '-j%{jobs}')"
%else
JFLAGS="$(echo '%{_smp_mflags}')"
%endif

make $JFLAGS

%install
rm -rf %{buildroot}
make install DESTDIR=%{buildroot}

test -d %{buildroot}/usr/sbin || mkdir %{buildroot}/usr/sbin
mv %{sap_script_prefix}-%{sap_hash}/sap_redhat_cluster_connector %{buildroot}/usr/sbin/sap_redhat_cluster_connector

## tree fixup
# remove docs (there is only one and they should come from doc sections in files)
rm -rf %{buildroot}/usr/share/doc/resource-agents

##
# Create symbolic link between IPAddr and IPAddr2
##
rm -f %{buildroot}/usr/lib/ocf/resource.d/heartbeat/IPaddr
ln -s /usr/lib/ocf/resource.d/heartbeat/IPaddr2 %{buildroot}/usr/lib/ocf/resource.d/heartbeat/IPaddr

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc AUTHORS COPYING COPYING.GPLv3 ChangeLog
%if %{with linuxha}
%doc doc/README.webapps
%doc %{_datadir}/%{name}/ra-api-1.dtd
%endif

%if %{with rgmanager}
%{_datadir}/cluster
%{_sbindir}/rhev-check.sh
%endif

%if %{with linuxha}
%dir /usr/lib/ocf
%dir /usr/lib/ocf/resource.d
%dir /usr/lib/ocf/lib

/usr/lib/ocf/lib/heartbeat

/usr/lib/ocf/resource.d/heartbeat
/usr/lib/ocf/resource.d/openstack
%if %{with rgmanager}
/usr/lib/ocf/resource.d/redhat
%endif

%if %{defined _unitdir}
%{_unitdir}/resource-agents-deps.target
%endif

%dir %{_datadir}/%{name}
%dir %{_datadir}/%{name}/ocft
%{_datadir}/%{name}/ocft/configs
%{_datadir}/%{name}/ocft/caselib
%{_datadir}/%{name}/ocft/README
%{_datadir}/%{name}/ocft/README.zh_CN

%{_sbindir}/ocft

%{_includedir}/heartbeat

%dir %attr (1755, root, root)	%{_var}/run/resource-agents

%{_mandir}/man7/*.7*

###
# Supported, but in another sub package
###
%exclude %{_sbindir}/sap_redhat_cluster_connector
%exclude %{_sbindir}/show_SAPHanaSR_attributes
%exclude /usr/lib/ocf/resource.d/heartbeat/SAP*
%exclude /usr/lib/ocf/lib/heartbeat/sap*
%exclude %{_mandir}/man7/*SAP*

###
# Unsupported
###
%exclude /usr/lib/ocf/resource.d/heartbeat/AoEtarget
%exclude /usr/lib/ocf/resource.d/heartbeat/AudibleAlarm
%exclude /usr/lib/ocf/resource.d/heartbeat/ClusterMon
%exclude /usr/lib/ocf/resource.d/heartbeat/EvmsSCC
%exclude /usr/lib/ocf/resource.d/heartbeat/Evmsd
%exclude /usr/lib/ocf/resource.d/heartbeat/ICP
%exclude /usr/lib/ocf/resource.d/heartbeat/LinuxSCSI
%exclude /usr/lib/ocf/resource.d/heartbeat/ManageRAID
%exclude /usr/lib/ocf/resource.d/heartbeat/ManageVE
%exclude /usr/lib/ocf/resource.d/heartbeat/Pure-FTPd
%exclude /usr/lib/ocf/resource.d/heartbeat/Raid1
%exclude /usr/lib/ocf/resource.d/heartbeat/ServeRAID
%exclude /usr/lib/ocf/resource.d/heartbeat/SphinxSearchDaemon
%exclude /usr/lib/ocf/resource.d/heartbeat/Stateful
%exclude /usr/lib/ocf/resource.d/heartbeat/SysInfo
%exclude /usr/lib/ocf/resource.d/heartbeat/VIPArip
%exclude /usr/lib/ocf/resource.d/heartbeat/WAS
%exclude /usr/lib/ocf/resource.d/heartbeat/WAS6
%exclude /usr/lib/ocf/resource.d/heartbeat/WinPopup
%exclude /usr/lib/ocf/resource.d/heartbeat/Xen
%exclude /usr/lib/ocf/resource.d/heartbeat/anything
%exclude /usr/lib/ocf/resource.d/heartbeat/asterisk
%exclude /usr/lib/ocf/resource.d/heartbeat/eDir88
%exclude /usr/lib/ocf/resource.d/heartbeat/fio
%exclude /usr/lib/ocf/resource.d/heartbeat/ids
%exclude /usr/lib/ocf/resource.d/heartbeat/iscsi
%exclude /usr/lib/ocf/resource.d/heartbeat/jboss
%exclude /usr/lib/ocf/resource.d/heartbeat/ldirectord
%exclude /usr/lib/ocf/resource.d/heartbeat/lxc
%exclude /usr/lib/ocf/resource.d/heartbeat/pingd
%exclude /usr/lib/ocf/resource.d/heartbeat/pound
%exclude /usr/lib/ocf/resource.d/heartbeat/proftpd
%exclude /usr/lib/ocf/resource.d/heartbeat/scsi2reservation
%exclude /usr/lib/ocf/resource.d/heartbeat/sfex
%exclude /usr/lib/ocf/resource.d/heartbeat/syslog-ng
%exclude /usr/lib/ocf/resource.d/heartbeat/varnish
%exclude /usr/lib/ocf/resource.d/heartbeat/vmware
%exclude /usr/lib/ocf/resource.d/heartbeat/zabbixserver
%exclude /usr/lib/ocf/resource.d/heartbeat/mysql-proxy
%exclude /usr/lib/ocf/resource.d/heartbeat/rsyslog
%exclude %{_mandir}/man7/ocf_heartbeat_AoEtarget.7.gz
%exclude %{_mandir}/man7/ocf_heartbeat_AudibleAlarm.7.gz
%exclude %{_mandir}/man7/ocf_heartbeat_ClusterMon.7.gz
%exclude %{_mandir}/man7/ocf_heartbeat_EvmsSCC.7.gz
%exclude %{_mandir}/man7/ocf_heartbeat_Evmsd.7.gz
%exclude %{_mandir}/man7/ocf_heartbeat_ICP.7.gz
%exclude %{_mandir}/man7/ocf_heartbeat_IPaddr.7.gz
%exclude %{_mandir}/man7/ocf_heartbeat_LinuxSCSI.7.gz
%exclude %{_mandir}/man7/ocf_heartbeat_ManageRAID.7.gz
%exclude %{_mandir}/man7/ocf_heartbeat_ManageVE.7.gz
%exclude %{_mandir}/man7/ocf_heartbeat_Pure-FTPd.7.gz
%exclude %{_mandir}/man7/ocf_heartbeat_Raid1.7.gz
%exclude %{_mandir}/man7/ocf_heartbeat_ServeRAID.7.gz
%exclude %{_mandir}/man7/ocf_heartbeat_SphinxSearchDaemon.7.gz
%exclude %{_mandir}/man7/ocf_heartbeat_Stateful.7.gz
%exclude %{_mandir}/man7/ocf_heartbeat_SysInfo.7.gz
%exclude %{_mandir}/man7/ocf_heartbeat_VIPArip.7.gz
%exclude %{_mandir}/man7/ocf_heartbeat_WAS.7.gz
%exclude %{_mandir}/man7/ocf_heartbeat_WAS6.7.gz
%exclude %{_mandir}/man7/ocf_heartbeat_WinPopup.7.gz
%exclude %{_mandir}/man7/ocf_heartbeat_Xen.7.gz
%exclude %{_mandir}/man7/ocf_heartbeat_anything.7.gz
%exclude %{_mandir}/man7/ocf_heartbeat_asterisk.7.gz
%exclude %{_mandir}/man7/ocf_heartbeat_eDir88.7.gz
%exclude %{_mandir}/man7/ocf_heartbeat_fio.7.gz
%exclude %{_mandir}/man7/ocf_heartbeat_ids.7.gz
%exclude %{_mandir}/man7/ocf_heartbeat_iscsi.7.gz
%exclude %{_mandir}/man7/ocf_heartbeat_jboss.7.gz
%exclude %{_mandir}/man7/ocf_heartbeat_lxc.7.gz
%exclude %{_mandir}/man7/ocf_heartbeat_pingd.7.gz
%exclude %{_mandir}/man7/ocf_heartbeat_pound.7.gz
%exclude %{_mandir}/man7/ocf_heartbeat_proftpd.7.gz
%exclude %{_mandir}/man7/ocf_heartbeat_scsi2reservation.7.gz
%exclude %{_mandir}/man7/ocf_heartbeat_sfex.7.gz
%exclude %{_mandir}/man7/ocf_heartbeat_syslog-ng.7.gz
%exclude %{_mandir}/man7/ocf_heartbeat_varnish.7.gz
%exclude %{_mandir}/man7/ocf_heartbeat_vmware.7.gz
%exclude %{_mandir}/man7/ocf_heartbeat_zabbixserver.7.gz
%exclude %{_mandir}/man7/ocf_heartbeat_mysql-proxy.7.gz
%exclude %{_mandir}/man7/ocf_heartbeat_rsyslog.7.gz

###
# Other excluded files.
###
# This tool has to be updated for the new pacemaker lrmd.
%exclude %{_sbindir}/ocf-tester
%exclude %{_mandir}/man8/ocf-tester.8*
# ldirectord is not supported
%exclude /etc/ha.d/resource.d/ldirectord
%exclude /etc/init.d/ldirectord
%exclude /etc/logrotate.d/ldirectord
%exclude /usr/sbin/ldirectord
%exclude %{_mandir}/man8/ldirectord.8.gz

# For compatability with pre-existing agents
%dir %{_sysconfdir}/ha.d
%{_sysconfdir}/ha.d/shellfuncs

%{_libexecdir}/heartbeat
%endif

%if %{with rgmanager}
%post -n resource-agents
ccs_update_schema > /dev/null 2>&1 ||:
%endif

%ifarch x86_64 ppc64le
%files sap
%defattr(-,root,root)
%{_sbindir}/sap_redhat_cluster_connector
/usr/lib/ocf/resource.d/heartbeat/SAP*
/usr/lib/ocf/lib/heartbeat/sap*
%{_mandir}/man7/*SAP*
%exclude %{_mandir}/man7/*SAPHana*
%exclude /usr/lib/ocf/resource.d/heartbeat/SAPHana*
%endif

%ifarch x86_64 ppc64le
%files sap-hana
%defattr(-,root,root)
/usr/lib/ocf/resource.d/heartbeat/SAPHana*
%{_mandir}/man7/*SAPHana*
%endif

%changelog
* Thu Sep 21 2017 Oyvind Albrigtsen <oalbrigt@redhat.com> - 3.9.5-105.1
- support per-host and per-bundle attributes

  Resolves: rhbz#1493915

* Fri Jun 23 2017 Oyvind Albrigtsen <oalbrigt@redhat.com> - 3.9.5-105
- rabbitmq-cluster: fix to keep expiration policy

  Resolves: rhbz#1342376

* Fri Jun  2 2017 Oyvind Albrigtsen <oalbrigt@redhat.com> - 3.9.5-104
- SAPHana/SAPHanaTopology: update to version 0.152.21

  Resolves: rhbz#1449681

* Wed May 31 2017 Oyvind Albrigtsen <oalbrigt@redhat.com> - 3.9.5-102
- LVM: update metadata on start/relocate
- LVM: warn when cache mode is not writethrough

  Resolves: rhbz#1451933

* Tue May 30 2017 Oyvind Albrigtsen <oalbrigt@redhat.com> - 3.9.5-101
- LVM: status check for missing VG

  Resolves: rhbz#1454699

* Mon May 22 2017 Oyvind Albrigtsen <oalbrigt@redhat.com> - 3.9.5-100
- docker: add "mount_points" parameter to be able to create directories

  Resolves: rhbz#1452049

* Tue May 16 2017 Oyvind Albrigtsen <oalbrigt@redhat.com> - 3.9.5-99
- galera: fix bootstrap when cluster has no data

  Resolves: rhbz#1451097

* Wed May  3 2017 Oyvind Albrigtsen <oalbrigt@redhat.com> - 3.9.5-97
- systemd: add drop-in for clvmd and LVM to avoid fencing on shutdown

  Resolves: rhbz#1316130

* Wed Apr 26 2017 Oyvind Albrigtsen <oalbrigt@redhat.com> - 3.9.5-96
- IPaddr2: add "preferred_lft" parameter for IPv6

  Resolves: rhbz#1445861

* Fri Apr  7 2017 Oyvind Albrigtsen <oalbrigt@redhat.com> - 3.9.5-95
- DB2: fix HADR for DB2 V98 or later

  Resolves: rhbz#1427574

* Tue Apr  4 2017 Oyvind Albrigtsen <oalbrigt@redhat.com> - 3.9.5-94
- send_arp: update usage info

  Resolves: rhbz#1380405

* Tue Apr  4 2017 Oyvind Albrigtsen <oalbrigt@redhat.com> - 3.9.5-93
- rabbitmq-cluster: allow to run on Pacemaker remote nodes
- oraasm: new resource agent for Oracle ASM

  Resolves: rhbz#1435982
  Resolves: rhbz#1411225

* Tue Mar 28 2017 Oyvind Albrigtsen <oalbrigt@redhat.com> - 3.9.5-90
- ethmonitor: fix to monitor interface without IP

  Resolves: rhbz#bz1408656

* Tue Mar 28 2017 Oyvind Albrigtsen <oalbrigt@redhat.com> - 3.9.5-89
- NodeUtilization: new resource agent
- iSCSILogicalUnit, iSCSITarget: make concurrent-safe
- IPaddr2: send gratuitious ARP packets during monitor action
- named: add support for rndc options
- CTDB: fix logging
- IPaddr2: add option to detect duplicate IP

  Resolves: rhbz#1430304
  Resolves: rhbz#1430385
  Resolves: rhbz#1434351
  Resolves: rhbz#1435171
  Resolves: rhbz#1077888
  Resolves: rhbz#1393189

* Thu Mar  9 2017 Oyvind Albrigtsen <oalbrigt@redhat.com> - 3.9.5-88
- clvm: remove reload action
- iSCSILogicalUnit: add IPv6-support
- IPsrcaddr: fix issue with duplicate routes
- pgsql: don't use crm_failcount
- ocf_log: use same log format as Pacemaker

  Resolves: rhbz#1359252
  Resolves: rhbz#1389300
  Resolves: rhbz#1400172
  Resolves: rhbz#1420565
  Resolves: rhbz#1427611

* Thu Feb  2 2017 Oyvind Albrigtsen <oalbrigt@redhat.com> - 3.9.5-87
- LVM: fix for "partial vg activates when partial_activation=false"
- redis: notify clients of master being demoted
- SAP/SAP HANA: ppc64le build

  Resolves: rhbz#1392432
  Resolves: rhbz#1305549
  Resolves: rhbz#1371088

* Fri Jan 27 2017 Oyvind Albrigtsen <oalbrigt@redhat.com> - 3.9.5-86
- SAPDatabase: fix process count for SUSER
- rabbitmq-cluster: reset Mnesia before join

  Resolves: rhbz#1260713
  Resolves: rhbz#1397393

* Fri Jan 13 2017 Oyvind Albrigtsen <oalbrigt@redhat.com> - 3.9.5-85
- exportfs: fix for IPv6 addresses
- SAPHana/SAPHanaTopology: update to version 0.152.17
- Add netstat dependency

  Resolves: rhbz#1406152
  Resolves: rhbz#1395142
  Resolves: rhbz#1402370

* Tue Dec 20 2016 Oyvind Albrigtsen <oalbrigt@redhat.com> - 3.9.5-84
- galera: prevent promote after demote
- iSCSITarget: properly create portals for lio-t
- nfsserver: dont stop rpcbind
- Filesystem: submount check
- Delay: change startdelay
- galera: last commit fix for MariaDB 10.1.18+
- portblock: return success on stop with invalid IP
- portblock: use iptables wait

  Resolves: rhbz#1360768
  Resolves: rhbz#1376588
  Resolves: rhbz#1384955
  Resolves: rhbz#1387363
  Resolves: rhbz#1388854
  Resolves: rhbz#1391470
  Resolves: rhbz#1391580
  Resolves: rhbz#1395596

* Tue Nov 29 2016 Oyvind Albrigtsen <oalbrigt@redhat.com> - 3.9.5-83
- nfsserver: keep options in /etc/sysconfig/nfs
- redis: fix SELinux permissions
- redis: notify clients of master being demoted

  Resolves: rhbz#1387491
  Resolves: rhbz#1390974
  Resolves: rhbz#1305549

* Tue Sep 20 2016 Oyvind Albrigtsen <oalbrigt@redhat.com> - 3.9.5-82
- portblock: create tickle_dir if it doesn't exist
- tomcat: use systemd if available

  Resolves: rhbz#1303037
  Resolves: rhbz#1249430

* Mon Aug 29 2016 Oyvind Albrigtsen <oalbrigt@redhat.com> - 3.9.5-81
- oracle: fix issue with C## in monprofile and inform user that
  monuser must start with C## as well for container databases

  Resolves: rhbz#1328386

* Wed Jul 27 2016 Andrew Beekhof <abeekhof@redhat.com> - 3.9.5-80
- rabbit: Allow automatic cluster recovery before forcing it

  Resolves: rhbz#1343905

* Fri Jul 22 2016 Oyvind Albrigtsen <oalbrigt@redhat.com> - 3.9.5-79
- oracle: use monprofile parameter

  Resolves: rhbz#1358895

* Thu Jul 21 2016 Oyvind Albrigtsen <oalbrigt@redhat.com> - 3.9.5-78
- nfsserver: fix monitor issues causing NFS to start on
  "debug-monitor" and "resource cleanup"
- nfsserver: remove "up to 10 tries" on start to avoid issues with
  some services taking longer to start
- nfsserver: stop rpc-gssd to allow unmounting of "rpcpipefs_dir"

  Resolves: rhbz#1356866
  Resolves: rhbz#1126073
  Resolves: rhbz#1346733

* Tue Jul  5 2016 Oyvind Albrigtsen <oalbrigt@redhat.com> - 3.9.5-77
- rabbitmq-cluster: add return codes for not running

  Resolves: rhbz#1342478

* Fri Jun 24 2016 Oyvind Albrigtsen <oalbrigt@redhat.com> - 3.9.5-76
- rabbitmq-cluster: support dump/restore users for RabbitMQ v. 3.6.x

  Resolves: rhbz#1343905

* Mon Jun  6 2016 Oyvind Albrigtsen <oalbrigt@redhat.com> - 3.9.5-73
- portblock: fix tickle_tcp bug
- nfsserver: use rpcpipefs_dir variable
- mysql: use replication_port variable
- oracle: inform user that monprofile must start with C## for
  container databases

  Resolves: rhbz#1337109
  Resolves: rhbz#1337615
  Resolves: rhbz#1337124
  Resolves: rhbz#1328386

* Fri Jun  3 2016 Damien Ciabrini <dciabrin@redhat.com> - 3.9.5-72
- garbd: Introduces garbd resource-agent

  Resolves: rhbz#1328018

* Fri May 13 2016 Oyvind Albrigtsen <oalbrigt@redhat.com> - 3.9.5-71
- nova-compute-wait: fix "Invalid Nova host name" issue

  Resolves: rhbz#1320783

* Tue May  3 2016 Oyvind Albrigtsen <oalbrigt@redhat.com> - 3.9.5-70
- nfsserver: fix nfs-idmapd fails to start due to
  var-lib-nfs-rpc_pipefs.mount being active

  Resolves: rhbz#1325453

* Tue Apr 26 2016 Oyvind Albrigtsen <oalbrigt@redhat.com> - 3.9.5-69
- SAP HANA: add Multiple Components One System (MCOS) support
- VirtualDomain: add migration_speed and migration_downtime options
- VirtualDomain: fix unnecessary error when probing nonexistent domain
- oralsnr: fix status check fail when username is more than 8 characters long
- oracle: fix unable to start because of ORA-01081

  Resolves: rhbz#1289107
  Resolves: rhbz#1296406
  Resolves: rhbz#1307160
  Resolves: rhbz#1317578
  Resolves: rhbz#1318985

* Thu Mar 17 2016 Damien Ciabrini <dciabrin@redhat.com> - 3.9.5-68
- galera: recover blocked nodes with --tc-heuristics-recover

  Resolves: rhbz#1284526

* Tue Mar  1 2016 Oyvind Albrigtsen <oalbrigt@redhat.com> - 3.9.5-67
- sap_redhat_cluster_connector: add support for hostnames with "-"
- NovaEvacuate: simplify nova check
- portblock: new resource agent

  Resolves: rhbz#1265527
  Resolves: rhbz#1287314
  Resolves: rhbz#1303037

* Tue Mar  1 2016 Peter Lemenkov <lemenkov@redhat.com> - 3.9.5-65
- RabbitMQ: keep users during resource reload (small regression fix)

  Resolves: rhbz#1303803

* Tue Mar  1 2016 Peter Lemenkov <lemenkov@redhat.com> - 3.9.5-64
- RabbitMQ: keep users during resource reload

  Resolves: rhbz#1303803

* Tue Mar  1 2016 Oyvind Albrigtsen <oalbrigt@redhat.com> - 3.9.5-63
- IPaddr2: use IPv6 DAD for collision detection
- nagios: new resource agent

  Resolves: rhbz#1276699
  Resolves: rhbz#1212632

* Mon Feb 29 2016 Oyvind Albrigtsen <oalbrigt@redhat.com> - 3.9.5-62
- tomcat: fix for SELinux enforced mode
- send_arp: fix buffer overflow on infiniband devices
- mysql: fix tmpfile leak
- VirtualDomain: add migrate_options parameter
- VirtualDomain: fix issue where config file might get removed
- VirtualDomain: fix locale in stop and status functions()

  Resolves: rhbz#1249430
  Resolves: rhbz#1250728
  Resolves: rhbz#1263348
  Resolves: rhbz#1242181
  Resolves: rhbz#1242558
  Resolves: rhbz#1301189

* Mon Feb 22 2016 Oyvind Albrigtsen <oalbrigt@redhat.com> - 3.9.5-60
- rabbitmq-cluster: fix to forget stopped cluster nodes
- nfsserver: fix systemd status detection

  Resolves: rhbz#1247303
  Resolves: rhbz#1126073

* Wed Feb  3 2016 Oyvind Albrigtsen <oalbrigt@redhat.com> - 3.9.5-57
- Replace NovaCompute with nova-compute-wait which lets systemd
  manage the nova-compute process

  Resolves: rhbz#1304011

* Wed Feb  3 2016 Oyvind Albrigtsen <oalbrigt@redhat.com> - 3.9.5-56
- galera: add custom host/port support

  Resolves: rhbz#1299404

* Tue Feb  2 2016 Oyvind Albrigtsen <oalbrigt@redhat.com> - 3.9.5-55
- NovaCompute/NovaEvacuate: Fix 'evacute' typo
- NovaEvacuate invoke off action

  Resolves: rhbz#1282723
  Resolves: rhbz#1287303

* Mon Sep  7 2015 Fabio M. Di Nitto <fdinitto@redhat.com> - 3.9.5-54
- Fix redis client password regexp
  Resolves: rhbz#1251484

* Thu Sep  3 2015 Fabio M. Di Nitto <fdinitto@redhat.com> - 3.9.5-53
- Add support redis client password authentication
  Resolves: rhbz#1251484

* Thu Jul 23 2015 David Vossel <dvossel@redhat.com> - 3.9.5-52
- Only build SAP hana packages for x86_64

  Resolves: rhbz#1244827

* Thu Jul 23 2015 David Vossel <dvossel@redhat.com> - 3.9.5-51
- Properly include SAP hana packages in correct subpackage.

  Resolves: rhbz#1244827

* Thu Jul 23 2015 David Vossel <dvossel@redhat.com> - 3.9.5-50
- Sync SAP Hana agents with upstream

  Resolves: rhbz#1244827

* Wed Jul 22 2015 David Vossel <dvossel@redhat.com> - 3.9.5-49
- Place SAP Hana agents in sap-hana subpackage

  Resolves: rhbz#1244827

* Fri Jul 10 2015 David Vossel <dvossel@redhat.com> - 3.9.5-48
- add support for oracle resource agents

  Resolves: rhbz#1232376

* Thu Jun 25 2015 David Vossel <dvossel@redhat.com> - 3.9.5-47
- NovaCompute and NovaEvacuate updates
- dhcpd chroot fix
- redis 0byte error fix

  Resolves: rhbz#1214360
  Resolves: rhbz#1227293
  Resolves: rhbz#1231032

* Thu Jun 25 2015 David Vossel <dvossel@redhat.com> - 3.9.5-46
- iface-vlan agent
- Allow partial activation when physical volumes are missing.
- Properly handle 'includes' during apache config parsing
- Support for NovaCompute resource-agent

  Resolves: rhbz#1160365
  Resolves: rhbz#1214781
  Resolves: rhbz#1223615
  Resolves: rhbz#1214360

* Wed Apr 29 2015 David Vossel <dvossel@redhat.com> - 3.9.5-45
- Fix clvmd usage of daemon_options
- Use better default nfsserver start timeouts
- Make nfsserver preserve options in /etc/sysconfig/nfs
- Add link_status_only option to ethmonitor agent
- Add support for nginx agent
- Add support for db2 agent
- CTDB agent updates

  Resolves: rhbz#1171162
  Resolves: rhbz#1173193
  Resolves: rhbz#1182787
  Resolves: rhbz#1213971
  Resolves: rhbz#1183136
  Resolves: rhbz#1059988
  Resolves: rhbz#1077888

* Tue Apr 28 2015 David Vossel <dvossel@redhat.com> - 3.9.5-44
- For IPsrcaddr, properly handle misconfiguration in a way that
  doesn't result in fencing.
- Return exit reason for invalid netmask in IPaddr2

  Resolves: rhbz#1200756
  Resolves: rhbz#773399

* Mon Apr 27 2015 David Vossel <dvossel@redhat.com> - 3.9.5-43
- Add activate_vgs option to clvmd to control activating volume
  groups

  Resolves: rhbz#1198681

* Thu Apr 23 2015 David Vossel <dvossel@redhat.com> - 3.9.5-42
- Improve galera resource-agent to not require use of read-only
  mode to retrieve last known write sequence number.

  Resolves: rhbz#1170376

* Thu Feb 5 2015 David Vossel <dvossel@redhat.com> - 3.9.5-41
- Support for redis resource-agent

  Resolves: rhbz#1189187

* Mon Jan 26 2015 David Vossel <dvossel@redhat.com> - 3.9.5-20.2
- Support for rabbitmq-cluster resource-agent

  Resolves: rhbz#1185754

* Fri Dec 19 2014 David Vossel <dvossel@redhat.com> - 3.9.5-40
- Remove usage of write_back from iSCSILogicalUnit

  Resolves: rhbz#1118029

* Thu Dec 11 2014 David Vossel <dvossel@redhat.com> - 3.9.5-39
- Updates spec file to include iscsi resources

  Resolves: rhbz#1118029

* Mon Oct 27 2014 David Vossel <dvossel@redhat.com> - 3.9.5-38
- Handle invalid monitor_cmd option for docker resource-agent

  Resolves: rhbz#1135026

* Sun Oct 26 2014 David Vossel <dvossel@redhat.com> - 3.9.5-37
- Rename docker agent's 'container' arg to 'name' to avoid confusion
  with pacemaker's metadata 'container' argument.
- Introduce monitor_cmd into docker agent.

  Resolves: rhbz#1135026

* Thu Oct 23 2014 David Vossel <dvossel@redhat.com> - 3.9.5-36
- Fixes cleaning up stale docker containers during stop if
  container instance failed.

  Resolves: rhbz#1135026

* Thu Oct 23 2014 David Vossel <dvossel@redhat.com> - 3.9.5-35
- Introduces docker resource-agent for managing docker containers.
  The docker agent is being released as tech preview.

  Resolves: rhbz#1135026

* Wed Oct 22 2014 David Vossel <dvossel@redhat.com> - 3.9.5-34
- Fixes mysql agents behavior when monitoring resource instance
  when environment validation fails.

  Resolves: rhbz#1138871

* Tue Sep 23 2014 David Vossel <dvossel@redhat.com> - 3.9.5-33
- Merges latest upstream patches for galera agent
- Merges latest upstream patchs for exit reason string

  Resolves: rhbz#1116166
  Resolves: rhbz#1128933

* Wed Sep 17 2014 David Vossel <dvossel@redhat.com> - 3.9.5-32
- Fixes iSCSILogicalUnit syntax error
- Fixes mysql stop operation when db storage is unavailable

  Resolves: rhbz#1118029
  Resolves: rhbz#1138871

* Mon Aug 25 2014 David Vossel <dvossel@redhat.com> - 3.9.5-31
- Man page updates give pcs config examples
- add iscsi agent support
- add infiniband support to ethmonitor
- add resource-agent support of exit reason string
- add safe umount option to Filesystem resource agent

  Resolves: rhbz#1058102
  Resolves: rhbz#1118029
  Resolves: rhbz#1122285
  Resolves: rhbz#1128933
  Resolves: rhbz#1095944

* Fri Aug 15 2014 David Vossel <dvossel@redhat.com> - 3.9.5-30
- Support monitor of lxc without requiring libvirt.
- Wait for filesystem modules to load during start.
- Warn users managing clustered LVM when lvmetad is in use.
- Restore VirtualDomain default start stop timeout values.
- Support exit reason string
- Auto set lvm locking type to clustered when clvmd is in use.

Resolves: rhbz# 1083041
Resolves: rhbz# 1083231
Resolves: rhbz# 1097593
Resolves: rhbz# 1105655
Resolves: rhbz# 1128933
Resolves: rhbz# 773395


* Fri Jul 18 2014 David Vossel <dvossel@redhat.com> - 3.9.5-29
- Support the check_user and check_passwd galera resource-agent
  options.
- Minor NFS agent updates.

  Resolves: rhbz#1116166
  Resolves: rhbz#1091101

* Thu Jul 10 2014 David Vossel <dvossel@redhat.com> - 3.9.5-28
- Updates to nfs server related agent.
- Introduces nfsnotify for sending NFSv3 NSM state change
  notifications allowing NFSv3 clients to reclaim locks.

  Resolves: rhbz#1091101

* Wed Jul 09 2014 David Vossel <dvossel@redhat.com> - 3.9.5-27
- Introducing the galera resource-agent.

  Resolves: rhbz#1116166

* Tue Mar 18 2014 David Vossel <dvossel@redhat.com> - 3.9.5-26
- Handle monitor qemu based VirtualDomain resources without
  requiring libvirtd even if configuration file does not
  contain an 'emulator' value pointing to the emulator binary.

  Resolves: rhbz#1060367

* Fri Feb 14 2014 David Vossel <dvossel@redhat.com> - 3.9.5-25
- Rename clvmd agent to clvm to avoid problems associated
  with having a resource-agent named the same exact name
  as the binary the agent manages.

  Resolves: rhbz#1064512

* Fri Feb 14 2014 David Vossel <dvossel@redhat.com> - 3.9.5-24
- Addition of the clvmd resource-agent
- Support monitoring qemu based VirtualDomain resources without
  requiring libvirtd to be running.

  Resolves: rhbz#1064512
  Resolves: rhbz#1060367

* Fri Jan 24 2014 Daniel Mach <dmach@redhat.com> - 3.9.5-23
- Mass rebuild 2014-01-24

* Mon Jan 20 2014 David Vossel <dvossel@redhat.com> - 3.9.5-22
- Fixes VirtualDomain config parse error.

  Resolves: rhbz#1029061

* Fri Dec 27 2013 Daniel Mach <dmach@redhat.com> - 3.9.5-21
- Mass rebuild 2013-12-27

* Tue Nov 26 2013 David Vossel <dvossel@redhat.com> - 3.9.5-20
- tomcat agent updates for pacemaker support
- slapd agent updates for pacemaker support
- Fixes missing etab file required for nfsserver

  Resolves: rhbz#1033016
  Resolves: rhbz#917681

* Wed Nov 20 2013 David Vossel <dvossel@redhat.com> - 3.9.5-19
- Add back the Delay agent.

  Resolves: rhbz#917681

* Thu Nov 07 2013 David Vossel <dvossel@redhat.com> - 3.9.5-18
- Remove support for (nginx, mysql-proxy, rsyslog). nginx and
  mysql-proxy are not a supported projects. Rsyslog is not an
  agent we will be supporting in an HA environment.

  Resolves: rhbz#917681

* Wed Nov 06 2013 David Vossel <dvossel@redhat.com> - 3.9.5-17
- Split send_ua utility out of IPv6addr.c source so it can be
  re-used in IPaddr2 without requiring cluster-glue.
- Fixes issue with pgsql and SAPInstance not setting transient
  attributes correctly when local corosync node name is not
  equal to 'uname -n'
- High: ocft: Fedora supported test cases

  Resolves: rhbz#917681

* Mon Oct 07 2013 David Vossel <dvossel@redhat.com> - 3.9.5-16
- Fixes issue with mysql agent not being able to set transient
  attributes on local node correctly.
- Fixes bash syntax error in VirtualDomain during 'stop'
- Fixes VirtualDomain default hypervisor usage.
- Fixes VirtualDomain 'start' of pre-defined domain

  Resolves: rhbz#917681
  Resolves: rhbz#1014641
  Resolves: rhbz#1016140

* Thu Sep 26 2013 David Vossel <dvossel@redhat.com> - 3.9.5-15
- Update VirtualDomain heartbeat agent for heartbeat merger.
- Includes upstream fixes for pacemaker_remote lxc test case.

  Resolves: rhbz#917681

* Thu Sep 12 2013 David Vossel <dvossel@redhat.com> - 3.9.5-14
- Add ability for apache agent to perform simple monitoring
  of server request/response without requiring server-status
  to be enabled.
- Fixes invalid return statement in LVM agent.
- Oracle TNS_ADMIN option 

  Resolves: rhbz#917806
  Resolves: rhbz#917681
  Resolves: rhbz#799065

* Mon Sep 9 2013 David Vossel <dvossel@redhat.com> - 3.9.5-13
- Use correct default config for apache
  Resolves: rhbz#1005924

* Tue Jul 30 2013 David Vossel <dvossel@redhat.com> - 3.9.5-12
- Symbolic links do not have file permissions.

* Tue Jul 30 2013 David Vossel <dvossel@redhat.com> - 3.9.5-11
- Fixes file permissions problem detected in rpmdiff test

* Tue Jul 30 2013 David Vossel <dvossel@redhat.com> - 3.9.5-10
- Removes ldirectord package
- Puts sap agents and connector script in subpackage
- exclude unsupported packages
- symlink ipaddr to ipaddr2 so only a single agent is supported

* Mon Jul 29 2013 David Vossel <dvossel@redhat.com> - 3.9.5-9
- Fixes more multi-lib problems.

* Mon Jul 29 2013 David Vossel <dvossel@redhat.com> - 3.9.5-8
- Add runtime dependencies section for Heartbeat agents.
- Fix multi-lib inconsistencies found during rpm diff testing.
- Add dist field back to rpm release name.

* Tue Jul 16 2013 David Vossel <dvossel@redhat.com> - 3.9.5-7
- Detect duplicate resources with the same volgrpname
  name when using exclusive activation with tags

  Resolves: # rhbz984054

* Tue Jun 18 2013 David Vossel <dvossel@redhat.com> - 3.9.5-6
- Restores rsctmp directory to upstream default.

* Tue Jun 18 2013 David Vossel <dvossel@redhat.com> - 3.9.5-5
- Merges redhat provider into heartbeat provider. Remove
  rgmanager's redhat provider.

  Resolves: rhbz#917681
  Resolves: rhbz#928890
  Resolves: rhbz#952716
  Resolves: rhbz#960555

* Tue Mar 12 2013 David Vossel <dvossel@redhat.com> - 3.9.5-4
- Fixes build system error with conditional logic involving
  IPv6addr.

* Mon Mar 11 2013 David Vossel <dvossel@redhat.com> - 3.9.5-3
- Fixes build dependency for pod2man when building against
  rhel-7.

* Mon Mar 11 2013 David Vossel <dvossel@redhat.com> - 3.9.5-2
- Resolves rhbz#915050

* Mon Mar 11 2013 David Vossel <dvossel@redhat.com> - 3.9.5-1
- New upstream release.

* Fri Nov 09 2012 Chris Feist <cfeist@redhat.com> - 3.9.2-5
- Fixed upstream tarball location

* Fri Nov 09 2012 Chris Feist <cfeist@redhat.com> - 3.9.2-4
- Removed version after dist tag
- Resolves: rhbz#875250

* Mon Oct 29 2012 Chris Feist <cfeist@redhat.com> - 3.9.2-3.8
- Remove cluster-glue-libs-devel
- Disable IPv6addr & sfex to fix deps on libplumgpl & libplum (due to
  disappearance of cluster-glue in F18)

* Sat Jul 21 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.9.2-3.5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Thu Jul  5 2012 Chris Feist <cfeist@redhat.com> - 3.9.2-3.4
- Fix location of lvm (change from /sbin to /usr/sbin)

* Wed Apr  4 2012 Jon Ciesla <limburgher@gmail.com> - 3.9.2-3.3
- Rebuilt to fix rawhide dependency issues (caused by move of fsck from
  /sbin to /usr/sbin).

* Fri Mar 30 2012 Jon Ciesla <limburgher@gmail.com> - 3.9.2-3.1
- libnet rebuild.

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.9.2-2.1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Fri Jul  8 2011 Fabio M. Di Nitto <fdinitto@redhat.com> - 3.9.2-2
- add post call to resource-agents to integrate with cluster 3.1.4

* Thu Jun 30 2011 Fabio M. Di Nitto <fdinitto@redhat.com> - 3.9.2-1
- new upstream release
- fix 2 regressions from 3.9.1

* Mon Jun 20 2011 Fabio M. Di Nitto <fdinitto@redhat.com> - 3.9.1-1
- new upstream release
- import spec file from upstream

* Tue Mar  1 2011 Fabio M. Di Nitto <fdinitto@redhat.com> - 3.1.1-1
- new upstream release 3.1.1 and 1.0.4

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.1.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Thu Dec  2 2010 Fabio M. Di Nitto <fdinitto@redhat.com> - 3.1.0-1
- new upstream release
- spec file update:
  Update upstream URL
  Update source URL
  use standard configure macro
  use standard make invokation

* Thu Oct  7 2010 Fabio M. Di Nitto <fdinitto@redhat.com> - 3.0.17-1
- new upstream release
  Resolves: rhbz#632595, rhbz#633856, rhbz#632385, rhbz#628013
  Resolves: rhbz#621313, rhbz#595383, rhbz#580492, rhbz#605733
  Resolves: rhbz#636243, rhbz#591003, rhbz#637913, rhbz#634718
  Resolves: rhbz#617247, rhbz#617247, rhbz#617234, rhbz#631943
  Resolves: rhbz#639018

* Thu Oct  7 2010 Andrew Beekhof <andrew@beekhof.net> - 3.0.16-2
- new upstream release of the Pacemaker agents: 71b1377f907c

* Thu Sep  2 2010 Fabio M. Di Nitto <fdinitto@redhat.com> - 3.0.16-1
- new upstream release
  Resolves: rhbz#619096, rhbz#614046, rhbz#620679, rhbz#619680
  Resolves: rhbz#621562, rhbz#621694, rhbz#608887, rhbz#622844
  Resolves: rhbz#623810, rhbz#617306, rhbz#623816, rhbz#624691
  Resolves: rhbz#622576

* Thu Jul 29 2010 Fabio M. Di Nitto <fdinitto@redhat.com> - 3.0.14-1
- new upstream release
  Resolves: rhbz#553383, rhbz#557563, rhbz#578625, rhbz#591003
  Resolves: rhbz#593721, rhbz#593726, rhbz#595455, rhbz#595547
  Resolves: rhbz#596918, rhbz#601315, rhbz#604298, rhbz#606368
  Resolves: rhbz#606470, rhbz#606480, rhbz#606754, rhbz#606989
  Resolves: rhbz#607321, rhbz#608154, rhbz#608887, rhbz#609181
  Resolves: rhbz#609866, rhbz#609978, rhbz#612097, rhbz#612110
  Resolves: rhbz#612165, rhbz#612941, rhbz#614127, rhbz#614356
  Resolves: rhbz#614421, rhbz#614457, rhbz#614961, rhbz#615202
  Resolves: rhbz#615203, rhbz#615255, rhbz#617163, rhbz#617566
  Resolves: rhbz#618534, rhbz#618703, rhbz#618806, rhbz#618814

* Mon Jun  7 2010 Fabio M. Di Nitto <fdinitto@redhat.com> - 3.0.13-1
- new upstream release
  Resolves: rhbz#592103, rhbz#593108, rhbz#578617, rhbz#594626
  Resolves: rhbz#594511, rhbz#596046, rhbz#594111, rhbz#597002
  Resolves: rhbz#599643

* Tue May 18 2010 Andrew Beekhof <andrew@beekhof.net> - 3.0.12-2
- libnet is not available on RHEL
- Do not package ldirectord on RHEL
  Resolves: rhbz#577264

* Mon May 10 2010 Fabio M. Di Nitto <fdinitto@redhat.com> - 3.0.12-1
- new upstream release
  Resolves: rhbz#585217, rhbz#586100, rhbz#581533, rhbz#582753
  Resolves: rhbz#582754, rhbz#585083, rhbz#587079, rhbz#588890
  Resolves: rhbz#588925, rhbz#583789, rhbz#589131, rhbz#588010
  Resolves: rhbz#576871, rhbz#576871, rhbz#590000, rhbz#589823

* Mon May 10 2010 Andrew Beekhof <andrew@beekhof.net> - 3.0.12-1
- New pacemaker agents upstream release: a7c0f35916bf
  + High: pgsql: properly implement pghost parameter
  + High: RA: mysql: fix syntax error
  + High: SAPInstance RA: do not rely on op target rc when monitoring clones (lf#2371)
  + High: set the HA_RSCTMP directory to /var/run/resource-agents (lf#2378)
  + Medium: IPaddr/IPaddr2: add a description of the assumption in meta-data
  + Medium: IPaddr: return the correct code if interface delete failed
  + Medium: nfsserver: rpc.statd as the notify cmd does not work with -v (thanks to Carl Lewis)
  + Medium: oracle: reduce output from sqlplus to the last line for queries (bnc#567815)
  + Medium: pgsql: implement "config" parameter
  + Medium: RA: iSCSITarget: follow changed IET access policy

* Wed Apr 21 2010 Fabio M. Di Nitto <fdinitto@redhat.com> - 3.0.11-1
- new upstream release
  Resolves: rhbz#583945, rhbz#581047, rhbz#576330, rhbz#583017
  Resolves: rhbz#583019, rhbz#583948, rhbz#584003, rhbz#582017
  Resolves: rhbz#555901, rhbz#582754, rhbz#582573, rhbz#581533
- Switch to file based Requires.
  Also address several other problems related to missing runtime
  components in different agents.
  With the current Requires: set, we guarantee all basic functionalities
  out of the box for lvm/fs/clusterfs/netfs/networking.
  Resolves: rhbz#570008

* Sat Apr 17 2010 Andrew Beekhof <andrew@beekhof.net> - 3.0.10-2
- New pacemaker agents upstream release
  + High: RA: vmware: fix set_environment() invocation (LF 2342)
  + High: RA: vmware: update to version 0.2
  + Medium: Filesystem: prefer /proc/mounts to /etc/mtab for non-bind mounts (lf#2388)
  + Medium: IPaddr2: don't bring the interface down on stop (thanks to Lars Ellenberg)
  + Medium: IPsrcaddr: modify the interface route (lf#2367)
  + Medium: ldirectord: Allow multiple email addresses (LF 2168)
  + Medium: ldirectord: fix setting defaults for configfile and ldirectord (lf#2328)
  + Medium: meta-data: improve timeouts in most resource agents
  + Medium: nfsserver: use default values (lf#2321)
  + Medium: ocf-shellfuncs: don't log but print to stderr if connected to a terminal
  + Medium: ocf-shellfuncs: don't output to stderr if using syslog
  + Medium: oracle/oralsnr: improve exit codes if the environment isn't valid
  + Medium: RA: iSCSILogicalUnit: fix monitor for STGT
  + Medium: RA: make sure that OCF_RESKEY_CRM_meta_interval is always defined (LF 2284)
  + Medium: RA: ManageRAID: require bash
  + Medium: RA: ManageRAID: require bash
  + Medium: RA: VirtualDomain: bail out early if config file can't be read during probe (Novell 593988)
  + Medium: RA: VirtualDomain: fix incorrect use of __OCF_ACTION
  + Medium: RA: VirtualDomain: improve error messages
  + Medium: RA: VirtualDomain: spin on define until we definitely have a domain name
  + Medium: Route: add route table parameter (lf#2335)
  + Medium: sfex: don't use pid file (lf#2363,bnc#585416)
  + Medium: sfex: exit with success on stop if sfex has never been started (bnc#585416)

* Fri Apr  9 2010 Fabio M. Di Nitto <fdinitto@redhat.com> - 3.0.10-1
- New rgmanager resource agents upstream release
  Resolves: rhbz#519491, rhbz#570525, rhbz#571806, rhbz#574027
  Resolves: rhbz#574215, rhbz#574886, rhbz#576322, rhbz#576335
  Resolves: rhbz#575103, rhbz#577856, rhbz#577874, rhbz#578249
  Resolves: rhbz#578625, rhbz#578626, rhbz#578628, rhbz#578626
  Resolves: rhbz#579621, rhbz#579623, rhbz#579625, rhbz#579626
  Resolves: rhbz#579059

* Wed Mar 24 2010 Andrew Beekhof <andrew@beekhof.net> - 3.0.9-2
- Resolves: rhbz#572993 - Patched build process to correctly generate ldirectord man page
- Resolves: rhbz#574732 - Add libnet-devel as a dependancy to ensure IPaddrv6 is built

* Mon Mar  1 2010 Fabio M. Di Nitto <fdinitto@redhat.com> - 3.0.9-1
- New rgmanager resource agents upstream release
  Resolves: rhbz#455300, rhbz#568446, rhbz#561862, rhbz#536902
  Resolves: rhbz#512171, rhbz#519491

* Mon Feb 22 2010 Fabio M. Di Nitto <fdinitto@redhat.com> - 3.0.8-1
- New rgmanager resource agents upstream release
  Resolves: rhbz#548133, rhbz#565907, rhbz#545602, rhbz#555901
  Resolves: rhbz#564471, rhbz#515717, rhbz#557128, rhbz#536157
  Resolves: rhbz#455300, rhbz#561416, rhbz#562237, rhbz#537201
  Resolves: rhbz#536962, rhbz#553383, rhbz#556961, rhbz#555363
  Resolves: rhbz#557128, rhbz#455300, rhbz#557167, rhbz#459630
  Resolves: rhbz#532808, rhbz#556603, rhbz#554968, rhbz#555047
  Resolves: rhbz#554968, rhbz#555047
- spec file update:
  * update spec file copyright date
  * use bz2 tarball

* Fri Jan 15 2010 Fabio M. Di Nitto <fdinitto@redhat.com> - 3.0.7-2
- Add python as BuildRequires

* Mon Jan 11 2010 Fabio M. Di Nitto <fdinitto@redhat.com> - 3.0.7-1
- New rgmanager resource agents upstream release
  Resolves: rhbz#526286, rhbz#533461

* Mon Jan 11 2010 Andrew Beekhof <andrew@beekhof.net> - 3.0.6-2
- Update Pacameker agents to upstream version: c76b4a6eb576
  + High: RA: VirtualDomain: fix forceful stop (LF 2283)
  + High: apache: monitor operation of depth 10 for web applications (LF 2234)
  + Medium: IPaddr2: CLUSTERIP/iptables rule not always inserted on failed monitor (LF 2281)
  + Medium: RA: Route: improve validate (LF 2232)
  + Medium: mark obsolete RAs as deprecated (LF 2244)
  + Medium: mysql: escalate stop to KILL if regular shutdown doesn't work

* Mon Dec 7 2009 Fabio M. Di Nitto <fdinitto@redhat.com> - 3.0.6-1
- New rgmanager resource agents upstream release
- spec file update:
  * use global instead of define
  * use new Source0 url
  * use %name macro more aggressively

* Mon Dec 7 2009 Andrew Beekhof <andrew@beekhof.net> - 3.0.5-2
- Update Pacameker agents to upstream version: bc00c0b065d9
  + High: RA: introduce OCF_FUNCTIONS_DIR, allow it to be overridden (LF2239)
  + High: doc: add man pages for all RAs (LF2237)
  + High: syslog-ng: new RA
  + High: vmware: make meta-data work and several cleanups (LF 2212)
  + Medium: .ocf-shellfuncs: add ocf_is_probe function
  + Medium: Dev: make RAs executable (LF2239)
  + Medium: IPv6addr: ifdef out the ip offset hack for libnet v1.1.4 (LF 2034)
  + Medium: add mercurial repository version information to .ocf-shellfuncs
  + Medium: build: add perl-MailTools runtime dependency to ldirectord package (LF 1469)
  + Medium: iSCSITarget, iSCSILogicalUnit: support LIO
  + Medium: nfsserver: use check_binary properly in validate (LF 2211)
  + Medium: nfsserver: validate should not check if nfs_shared_infodir exists (thanks to eelco@procolix.com) (LF 2219)
  + Medium: oracle/oralsnr: export variables properly
  + Medium: pgsql: remove the previous backup_label if it exists
  + Medium: postfix: fix double stop (thanks to Dinh N. Quoc)
  + RA: LVM: Make monitor operation quiet in logs (bnc#546353)
  + RA: Xen: Remove instance_attribute "allow_migrate" (bnc#539968)
  + ldirectord: OCF agent: overhaul

* Fri Nov 20 2009 Fabio M. Di Nitto <fdinitto@redhat.com> - 3.0.5-1
- New rgmanager resource agents upstream release
- Allow pacemaker to use rgmanager resource agents

* Wed Oct 28 2009 Andrew Beekhof <andrew@beekhof.net> - 3.0.4-2
- Update Pacameker agents to upstream version: e2338892f59f
  + High: send_arp - turn on unsolicited mode for compatibilty with the libnet version's exit codes
  + High: Trap sigterm for compatibility with the libnet version of send_arp
  + Medium: Bug - lf#2147: IPaddr2: behave if the interface is down
  + Medium: IPv6addr: recognize network masks properly
  + Medium: RA: VirtualDomain: avoid needlessly invoking "virsh define"

* Wed Oct 21 2009 Fabio M. Di Nitto <fdinitto@redhat.com> - 3.0.4-1
- New rgmanager resource agents upstream release

* Mon Oct 12 2009 Andrew Beekhof <andrew@beekhof.net> - 3.0.3-3
- Update Pacameker agents to upstream version: 099c0e5d80db
  + Add the ha_parameter function back into .ocf-shellfuncs.
  + Bug bnc#534803 - Provide a default for MAILCMD
  + Fix use of undefined macro @HA_NOARCHDATAHBDIR@
  + High (LF 2138): IPsrcaddr: replace 0/0 with proper ip prefix (thanks to Michael Ricordeau and Michael Schwartzkopff)
  + Import shellfuncs from heartbeat as badly written RAs use it
  + Medium (LF 2173): nfsserver: exit properly in nfsserver_validate
  + Medium: RA: Filesystem: implement monitor operation
  + Medium: RA: VirtualDomain: loop on status if libvirtd is unreachable
  + Medium: RA: VirtualDomain: loop on status if libvirtd is unreachable (addendum)
  + Medium: RA: iSCSILogicalUnit: use a 16-byte default SCSI ID
  + Medium: RA: iSCSITarget: be more persistent deleting targets on stop
  + Medium: RA: portblock: add per-IP filtering capability
  + Medium: mysql-proxy: log_level and keepalive parameters
  + Medium: oracle: drop spurious output from sqlplus
  + RA: Filesystem: allow configuring smbfs mounts as clones

* Wed Sep 23 2009 Fabio M. Di Nitto <fdinitto@redhat.com> - 3.0.3-1
- New rgmanager resource agents upstream release

* Thu Aug 20 2009 Fabio M. Di Nitto <fdinitto@redhat.com> - 3.0.1-1
- New rgmanager resource agents upstream release

* Tue Aug 18 2009 Andrew Beekhof <andrew@beekhof.net> - 3.0.0-16
- Create an ldirectord package
- Update Pacameker agents to upstream version: 2198dc90bec4
  + Build: Import ldirectord.
  + Ensure HA_VARRUNDIR has a value to substitute
  + High: Add findif tool (mandatory for IPaddr/IPaddr2)
  + High: IPv6addr: new nic and cidr_netmask parameters
  + High: postfix: new resource agent
  + Include license information
  + Low (LF 2159): Squid: make the regexp match more precisely output of netstat
  + Low: configure: Fix package name.
  + Low: ldirectord: add dependency on $remote_fs.
  + Low: ldirectord: add mandatory required header to init script.
  + Medium (LF 2165): IPaddr2: remove all colons from the mac address before passing it to send_arp
  + Medium: VirtualDomain: destroy domain shortly before timeout expiry
  + Medium: shellfuncs: Make the mktemp wrappers work.
  + Remove references to Echo function
  + Remove references to heartbeat shellfuncs.
  + Remove useless path lookups
  + findif: actually include the right header. Simplify configure.
  + ldirectord: Remove superfluous configure artifact.
  + ocf-tester: Fix package reference and path to DTD.

* Tue Aug 11 2009 Ville Skyttä <ville.skytta@iki.fi> - 3.0.0-15
- Use bzipped upstream hg tarball.

* Wed Jul 29 2009 Fabio M. Di Nitto <fdinitto@redhat.com> - 3.0.0-14
- Merge Pacemaker cluster resource agents:
  * Add Source1.
  * Drop noarch. We have real binaries now.
  * Update BuildRequires.
  * Update all relevant prep/build/install/files/description sections.

* Sun Jul 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.0.0-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Wed Jul  8 2009 Fabio M. Di Nitto <fdinitto@redhat.com> - 3.0.0-12
- spec file updates:
  * Update copyright header
  * final release.. undefine alphatag

* Thu Jul  2 2009 Fabio M. Di Nitto <fdinitto@redhat.com> - 3.0.0-11.rc4
- New upstream release.

* Sat Jun 20 2009 Fabio M. Di Nitto <fdinitto@redhat.com> - 3.0.0-10.rc3
- New upstream release.

* Wed Jun 10 2009 Fabio M. Di Nitto <fdinitto@redhat.com> - 3.0.0-9.rc2
- New upstream release + git94df30ca63e49afb1e8aeede65df8a3e5bcd0970

* Tue Mar 24 2009 Fabio M. Di Nitto <fdinitto@redhat.com> - 3.0.0-8.rc1
- New upstream release.
- Update BuildRoot usage to preferred versions/names

* Mon Mar  9 2009 Fabio M. Di Nitto <fdinitto@redhat.com> - 3.0.0-7.beta1
- New upstream release.

* Fri Mar  6 2009 Fabio M. Di Nitto <fdinitto@redhat.com> - 3.0.0-6.alpha7
- New upstream release.

* Tue Mar  3 2009 Fabio M. Di Nitto <fdinitto@redhat.com> - 3.0.0-5.alpha6
- New upstream release.

* Tue Feb 24 2009 Fabio M. Di Nitto <fdinitto@redhat.com> - 3.0.0-4.alpha5
- Drop Conflicts with rgmanager.

* Mon Feb 23 2009 Fabio M. Di Nitto <fdinitto@redhat.com> - 3.0.0-3.alpha5
- New upstream release.

* Thu Feb 19 2009 Fabio M. Di Nitto <fdinitto@redhat.com> - 3.0.0-2.alpha4
- Add comments on how to build this package.

* Thu Feb  5 2009 Fabio M. Di Nitto <fdinitto@redhat.com> - 3.0.0-1.alpha4
- New upstream release.
- Fix datadir/cluster directory ownership.

* Tue Jan 27 2009 Fabio M. Di Nitto <fdinitto@redhat.com> - 3.0.0-1.alpha3
  - Initial packaging
