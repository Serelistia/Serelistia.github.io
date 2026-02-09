<?xml version="1.0" encoding="UTF-8"?>
<xsl:stylesheet
    xmlns:xsl="http://www.w3.org/1999/XSL/Transform"
    xmlns:math="http://www.w3.org/2005/xpath-functions/math"
    xmlns:xd="http://www.oxygenxml.com/ns/doc/xsl"
    xmlns:xs="http://www.w3.org/2001/XMLSchema"
    xmlns="http://www.w3.org/1999xhtml"
    exclude-result-prefixes="xs math xd"
    xpath-default-namespace="http://www.tei-c.org/ns/1.0"
    version="3.0">
    
    <xd:doc scope="stylesheet">
        <xd:desc>
            <xd:p><xd:b>Created on:</xd:b> Feb 8, 2026</xd:p>
            <xd:p><xd:b>Author:</xd:b> bob</xd:p>
            <xd:p></xd:p>
        </xd:desc>
    </xd:doc>
    
    <xsl:output method="xhtml"
        html-version="5"
        omit-xml-declaration="yes"
        include-content-type="no"
        indent="yes"/>
    
    <xsl:strip-space elements="day month year"/>
    
    <xsl:preserve-space elements="p li name"/>
    
    
</xsl:stylesheet>

