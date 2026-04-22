<xsl:stylesheet xmlns:xsl="http://www.w3.org/1999/XSL/Transform" version="1.0">
    <xsl:template match="/">
        <html lang="es">
            <head>
                <meta charset="UTF-8" />
                <title>Menú del Día</title>
            </head>
            <body>
                <h1>Menú del Día</h1>
                <xsl:apply-templates select="menu/categoria" />
            </body>
        </html>
    </xsl:template>

    <xsl:template match="categoria">
        <h2>
            <xsl:value-of select="@nombre" />
        </h2>
        <ul>
            <xsl:apply-templates select="plato" />
        </ul>
    </xsl:template>
    <xsl:template match="plato">
        <li>
            <xsl:value-of select="nombre" />
            <xsl:text> - </xsl:text>
            <xsl:value-of select="precio" />
            <xsl:text>€</xsl:text>
        </li>
    </xsl:template>
</xsl:stylesheet>