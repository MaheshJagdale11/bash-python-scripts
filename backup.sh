#!/bin/bash
SRC_DIR="/var/www/html"
DEST_DIR="/backup"
tar -czf $DEST_DIR/backup-$(date +%F).tar.gz $SRC_DIR
